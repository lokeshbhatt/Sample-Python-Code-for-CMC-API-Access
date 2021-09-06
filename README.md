#
#
# DISCLAIMER
ALL CODE IS PROVIDED "AS IS," WITH NO WARRANTIES OR GUARANTEES WHATSOEVER.  IBM EXPRESSLY DISCLAIMS TO THE  FULLEST EXTENT PERMITTED BY LAW ALL EXPRESS, IMPLIED,  STATUTORY AND OTHER WARRANTIES, GUARANTEES, OR  REPRESENTATIONS, INCLUDING, WITHOUT LIMITATION, THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR  PURPOSE, AND NON-INFRINGEMENT OF PROPRIETARY AND INTELLECTUAL PROPERTY RIGHTS.  YOU UNDERSTAND AND AGREE THAT  YOU USE THESE MATERIALS, INFORMATION, PRODUCTS, SOFTWARE, PROGRAMS, AND SERVICES, AT YOUR OWN DISCRETION AND  RISK AND THAT YOU WILL BE SOLELY RESPONSIBLE FOR ANY DAMAGES THAT MAY RESULT, INCLUDING LOSS OF DATA OR DAMAGE TO YOUR COMPUTER SYSTEM.
#
#
# Sample-Python-Code-for-CMC-API-Access
#
#
# Background
- The Cloud Management Console (CMC) runs as a service hosted in the IBM cloud, freeing organizations from maintaining software to monitor infrastructure.  
- CMC can be accessed from the comfort of most modern browsers for dynamic views of performance, inventory and logging for your complete Power Systems™ enterprise, whether on premises or off premises, simplifies and unifies information in a single location.  
-  This allows clients to easily make more informed decisions. As private and hybrid cloud deployments grow, enterprises need new insight into these environments.  
-  Tools that provide consolidated information and analytics can be key enablers to smooth operation of infrastructure.  
-  Refer [https://www.ibm.com/products/cloud-management-console](https://www.ibm.com/products/cloud-management-console)
#
#
# Use Case  
- Clients often run tools, programs & utlities to achieve a consolidated view of enterprise wide inventory, usage, credits etc.   
- Populating central dashboard with latest data points requires programatic access to end-point(CMC instance, in our case).   
#
#
# Introduction   
- Detailed here is a python based programatic approach to pull inventory, pool usage & credit data points using CMC APIs.   
- Code demonstrates an interactive menu based approach, but same can be easily modified/extended for equivalent command line / scheduled friendly code.   
- Refer picture below for detaild on techical framework observed and steps involved,   
![Alt text](https://github.com/lokeshbhatt/Sample-Python-Code-for-CMC-API-Access/blob/main/sample-python-code-for-cmc-api-access-framework.JPG "Sample Python Code for CMC API  Access Framework")
#
#
# Pre-requisites   
- Python3.5 (or latest) with required modules (sys, os, platform, requests, json, time, timedelta, datetime, dateutil.parser)   
- Internet connectivity   
- Permission to write/create files into current directory   
- CMC API Controller Access Parameters   
  -  BaseURL:   
  -  X-CMC-Client-Secret:  
  -  X-CMC-Client-Id:   
  -  **NOTE**:   
     1. Above must be saved in file named "parameters.json" in directory where code is kept.    
     2. Refer [SAMPLE parameters.json](https://github.com/lokeshbhatt/Sample-Python-Code-for-CMC-API-Access/blob/main/parameters.json "parameters.json") and raplace hint string <> with your CMC instance specific values.    
#   
#   
# How to run
1. Ensure you have all the pre-requisites met
2. Download and save [sample-python-code-for-cmc-api-access.py](https://github.com/lokeshbhatt/Sample-Python-Code-for-CMC-API-Access/blob/main/sample-python-code-for-cmc-api-access.py) at same location where fuly filled [SAMPLE parameters.json](https://github.com/lokeshbhatt/Sample-Python-Code-for-CMC-API-Access/blob/main/parameters.json "parameters.json") is kept.
3. Execute using "python sample-python-code-for-cmc-api-access.py".
4. Following the menu.  
? - YOU TUBE VIDEO LINK
#
#
# In case of error
- Open a command prompt
- Go to directory where pre-compiled binary is downloaded
- Execute from command line
- Save error code into a .txt file and share
#
#
# Downloads
- [sample-python-code-for-cmc-api-access.py](https://github.com/lokeshbhatt/Sample-Python-Code-for-CMC-API-Access/blob/main/sample-python-code-for-cmc-api-access.py)
- [SAMPLE parameters.json](https://github.com/lokeshbhatt/Sample-Python-Code-for-CMC-API-Access/blob/main/parameters.json "parameters.json")
#
#
# DISCLAIMER
ALL CODE IS PROVIDED "AS IS," WITH NO WARRANTIES OR GUARANTEES WHATSOEVER.  IBM EXPRESSLY DISCLAIMS TO THE  FULLEST EXTENT PERMITTED BY LAW ALL EXPRESS, IMPLIED,  STATUTORY AND OTHER WARRANTIES, GUARANTEES, OR  REPRESENTATIONS, INCLUDING, WITHOUT LIMITATION, THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR  PURPOSE, AND NON-INFRINGEMENT OF PROPRIETARY AND INTELLECTUAL PROPERTY RIGHTS.  YOU UNDERSTAND AND AGREE THAT  YOU USE THESE MATERIALS, INFORMATION, PRODUCTS, SOFTWARE, PROGRAMS, AND SERVICES, AT YOUR OWN DISCRETION AND  RISK AND THAT YOU WILL BE SOLELY RESPONSIBLE FOR ANY DAMAGES THAT MAY RESULT, INCLUDING LOSS OF DATA OR DAMAGE TO YOUR COMPUTER SYSTEM.
#
#
