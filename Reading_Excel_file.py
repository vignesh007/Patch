#!/usr/bin/env python3
import openpyxl
import yaml
import os
import time
import json
import calendar
from datetime import datetime

try:

     cmd = "git --version"
     print(os.system(''))
     #os.system ('ansible-playbook /var/lib/awx/projects/_18__snow_project/Change_creation.yml') 
     returned_value = os.system(cmd)  # returns the exit code in unix
     print('returned value:', returned_value)

except:
    print("error occured")
    raise 
