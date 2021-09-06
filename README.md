#
#
### ALL CODE IS PROVIDED "AS IS," WITH NO WARRANTIES OR GUARANTEES WHATSOEVER.  IBM EXPRESSLY DISCLAIMS TO THE  FULLEST EXTENT PERMITTED BY LAW ALL EXPRESS, IMPLIED,  STATUTORY AND OTHER WARRANTIES, GUARANTEES, OR  REPRESENTATIONS, INCLUDING, WITHOUT LIMITATION, THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR  PURPOSE, AND NON-INFRINGEMENT OF PROPRIETARY AND INTELLECTUAL PROPERTY RIGHTS.  YOU UNDERSTAND AND AGREE THAT  YOU USE THESE MATERIALS, INFORMATION, PRODUCTS, SOFTWARE, PROGRAMS, AND SERVICES, AT YOUR OWN DISCRETION AND  RISK AND THAT YOU WILL BE SOLELY RESPONSIBLE FOR ANY DAMAGES THAT MAY RESULT, INCLUDING LOSS OF DATA OR DAMAGE TO YOUR COMPUTER SYSTEM.
#
#
# Sample-Python-Code-for-CMC-API-Access
#
#
# Background
### The Cloud Management Console (CMC) runs as a service hosted in the IBM cloud, freeing organizations from maintaining software to monitor infrastructure.
### CMC can be accessed from the comfort of most modern browsers for dynamic views of performance, inventory and logging for your complete Power Systems™ enterprise, whether on premises or off premises, simplifies and unifies information in a single location.
### This allows clients to easily make more informed decisions. As private and hybrid cloud deployments grow, enterprises need new insight into these environments.
### Tools that provide consolidated information and analytics can be key enablers to smooth operation of infrastructure.
#
#
# Introduction
###    - Clients often run tools, programs & utlities to achieve a consolidated view of enterprise wide inventory, usage, credits etc.
###    - Populating central dashboard with latest data points requires programatic access to end-point's, CMC data points, in our case.
###    - Detaield here is a python based programatic approach to pull inventory, pool usage & credit data points using CMC APIs.
###    - Code demonstrates an interactive menu based approach, but same can be easily modified/extended for equivalent command line / scheduled friendly code.
example of pulling following data point using CMC APIs,
# cmc_apis_demo-0.0.py
#   - Sample code to fetch data using CMC APIs
# Change Log
#   - 0.0
#       -- Fetch following data points from provided CMC instance
#           --- Inventory
#           --- Usage pools
#           --- Usage tags
#


How to run frozen binary (.exe) - For Win10 ONLY
================================================
1. Double click on "cmc_apis_demo-0.0.exe", classic windows execution :)


How to run python program file
==============================
1. Open .py file
2. Install all the modules listed at the top of file
3. Ensure "parameters.json" file is populated appropriately
3. Execute using "python3 cmc_apis_demo-0.0.py"
