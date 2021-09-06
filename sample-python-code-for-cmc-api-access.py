import sys
import os
import platform
import requests
import json
import time
from timedelta import Timedelta
from datetime import datetime
import dateutil.parser
#########################################################################
#
# PROGRAM NAME: sample-python-code-for-cmc-api-access
#
######################### START: DISCLAIMER #############################
#
# DISCLAIMER
# ALL CODE IS PROVIDED "AS IS," WITH NO WARRANTIES OR GUARANTEES WHATSOEVER.
# IBM EXPRESSLY DISCLAIMS TO THE  FULLEST EXTENT PERMITTED BY LAW ALL EXPRESS,
# IMPLIED,  STATUTORY AND OTHER WARRANTIES, GUARANTEES, OR  REPRESENTATIONS,
# INCLUDING, WITHOUT LIMITATION, THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR  PURPOSE, AND NON-INFRINGEMENT OF PROPRIETARY AND
# INTELLECTUAL PROPERTY RIGHTS.  YOU UNDERSTAND AND AGREE THAT  YOU USE THESE
# MATERIALS, INFORMATION, PRODUCTS, SOFTWARE, PROGRAMS, AND SERVICES, AT YOUR
# OWN DISCRETION AND  RISK AND THAT YOU WILL BE SOLELY RESPONSIBLE FOR ANY
# DAMAGES THAT MAY RESULT, INCLUDING LOSS OF DATA OR DAMAGE TO YOUR COMPUTER
# SYSTEM.
#
########################## END: DISCLAIMER ##############################
#
# Change Log
#   - 0.0
#       -- Fetch following data points from provided CMC instance
#           --- Inventory
#           --- Usage pools
#           --- Usage tags
#
#########################################################################


InventoryURL="/v1/ep/inventory/tags"
PoolsURL="/v1/ep/usage/pools"
UsageURL="/v1/ep/usage/tags"

BaseURL=""
XCMCClientSecret=""
XCMCClientId=""

def PrintHeader():
    print()
    os.system("{}".format('cls' if platform.system().lower()=="windows" else 'clear'))
    print("".center(80, "#"))
    print(("  CMC APIs Usage Demo  ").center(80, "#"))
    print("".center(80, "#"))
    print()


def ExitMessage():
    print()
    print("Thanks for using !")
    print("Please share you feedback, issues & change requests.")
    print()
    res=input("")
    sys.exit(0)


def Initialize():
    global BaseURL
    global XCMCClientSecret
    global XCMCClientId
    ParameterFile="parameters.json"
    if not (os.path.isfile(ParameterFile) and os.path.getsize(ParameterFile) > 0):
        print("ERROR - parameters.json file not found !")
        ExitMessage()
    else:
        with open(ParameterFile, 'r') as outfile:
            ParameterFileJSON=json.load(outfile)
        BaseURL=ParameterFileJSON["Parameters"]["BaseURL"]
        XCMCClientSecret=ParameterFileJSON["Parameters"]["X-CMC-Client-Secret"]
        XCMCClientId=ParameterFileJSON["Parameters"]["X-CMC-Client-Id"]


def return_json(URL):
    headers = {"X-CMC-Client-Secret": XCMCClientSecret, "X-CMC-Client-Id": XCMCClientId}
    response = requests.get(URL, headers=headers)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e)
    json_obj = response.json()
    return json_obj


def Inventory():
    URL=BaseURL+InventoryURL
    print("Starting Inventory Data Collection ::",end="")
    InventoryJSON=return_json(URL)
    with open('inventory.json', 'w', encoding='utf-8') as f:
        json.dump(InventoryJSON, f, ensure_ascii=False, indent=4)
    print(" DONE (refer inventory.json file).")
    res=input()


def PoolsData():
    FreqList=["Hourly", "Daily", "Weekly","Monthly"]
    while True:
        PrintHeader()
        print("Select Pool Data Frequency")
        print("\t1. Hourly")
        print("\t2. Daily")
        print("\t3. Weekly")
        print("\t4. Monthly")
        print("\t9. Exit")
        print("\n\n\n\n\n\n\n")
        print("".center(80, "#"))
        print()
        res=int(input("Enter your choice : "))
        if res in [1,2,3,5]:
            Frequency=FreqList[res-1]
            break
        elif res==9:
            ExitMessage()
        else:
            res=input("\nWrong choice entered. Press any key to continue")

    while True:
        PrintHeader()
        print("Pools Data (Frequency=",Frequency,")",sep="")
        print()
        print("Select Pool Data Duration")
        print("\t1. Last 24 Hours")
        print("\t2. Last 1 week")
        print("\t3. Last 1 month")
        print("\t9. Exit")
        print("\n\n\n\n\n\n\n")
        print("".center(80, "#"))
        print()
        res=int(input("Enter your choice : "))
        if res==1:
            EndTS="".join(list(datetime.isoformat(datetime.utcnow()))[:19])+"Z"
            StartTS="".join(list(datetime.isoformat(datetime.utcnow()-Timedelta(days=1)))[:19])+"Z"
            break
        elif res==2:
            EndTS="".join(list(datetime.isoformat(datetime.utcnow()))[:19])+"Z"
            StartTS="".join(list(datetime.isoformat(datetime.utcnow()-Timedelta(days=7)))[:19])+"Z"
            break
        elif res==3:
            EndTS="".join(list(datetime.isoformat(datetime.utcnow()))[:19])+"Z"
            StartTS="".join(list(datetime.isoformat(datetime.utcnow()-Timedelta(days=30)))[:19])+"Z"
        elif res==9:
            ExitMessage()
        else:
            res=input("\nWrong choice entered. Press any key to continue")

    URL=BaseURL + PoolsURL  +"?EndTS=" + EndTS + "&Frequency=" + Frequency+ "&StartTS=" + StartTS
    print("Starting Usage Pools Data Collection ::",end="")
    PoolsJSON=return_json(URL)
    with open('pools.json', 'w', encoding='utf-8') as f:
        json.dump(PoolsJSON, f, ensure_ascii=False, indent=4)
    print(" DONE (refer pools.json file).")
    res=input()


def UsageData():
    FreqList=["Hourly", "Daily", "Weekly","Monthly"]
    while True:
        PrintHeader()
        print("Select Usage Data Frequency")
        print("\t1. Hourly")
        print("\t2. Daily")
        print("\t3. Weekly")
        print("\t4. Monthly")
        print("\t9. Exit")
        print("\n\n\n\n\n\n\n")
        print("".center(80, "#"))
        print()
        res=int(input("Enter your choice : "))
        if res in [1,2,3,5]:
            Frequency=FreqList[res-1]
            break
        elif res==9:
            ExitMessage()
        else:
            res=input("\nWrong choice entered. Press any key to continue")

    while True:
        PrintHeader()
        print("Usage Data (Frequency=",Frequency,")",sep="")
        print()
        print("Select Usage Data Duration")
        print("\t1. Last 24 Hours")
        print("\t2. Last 1 week")
        print("\t3. Last 1 month")
        print("\t9. Exit")
        print("\n\n\n\n\n\n\n")
        print("".center(80, "#"))
        print()
        res=int(input("Enter your choice : "))
        if res==1:
            EndTS="".join(list(datetime.isoformat(datetime.utcnow()))[:19])+"Z"
            StartTS="".join(list(datetime.isoformat(datetime.utcnow()-Timedelta(days=1)))[:19])+"Z"
            break
        elif res==2:
            EndTS="".join(list(datetime.isoformat(datetime.utcnow()))[:19])+"Z"
            StartTS="".join(list(datetime.isoformat(datetime.utcnow()-Timedelta(days=7)))[:19])+"Z"
            break
        elif res==3:
            EndTS="".join(list(datetime.isoformat(datetime.utcnow()))[:19])+"Z"
            StartTS="".join(list(datetime.isoformat(datetime.utcnow()-Timedelta(days=30)))[:19])+"Z"
        elif res==9:
            ExitMessage()
        else:
            res=input("\nWrong choice entered. Press any key to continue")

    URL=BaseURL + UsageURL  +"?EndTS=" + EndTS + "&Frequency=" + Frequency+ "&StartTS=" + StartTS
    print("Starting Usage Tags Data Collection ::",end="")
    UsageJSON=return_json(URL)
    with open('usage.json', 'w', encoding='utf-8') as f:
        json.dump(UsageJSON, f, ensure_ascii=False, indent=4)
    print(" DONE (refer usage.json file).")
    res=input()
    
    
Func = {"1": Inventory,
        "2": PoolsData,
        "3": UsageData,       
        "9": ExitMessage}


def main():
    Initialize()
    while True:
        PrintHeader()
        print("1. Fetch Inventory Data")
        print("2. Fetch Usage Pools Data")
        print("3. Fetch Usage Tags Data")
        print("9. Exit")
        print("\n\n\n\n\n\n\n")
        print("".center(80, "#"))
        print()
        res=input("Enter your choice : ")
        if res in Func:
            Func[res]()
        else:
            res=input("\nWrong choice entered. Press any key to continue")


if __name__ == "__main__":
    main()
