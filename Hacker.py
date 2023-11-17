import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr


Bl='\033[30m'
Re='\033[1;31m'
Gr='\033[1;32m'
Ye='\033[1;33m'
Blu='\033[1;34m'
Mage='\033[1;35m'
Cy='\033[1;36m'
Wh='\033[1;37m'

os.system('clear')
stderr.writelines(f"""{Gr}


██╗███████╗██╗  ██╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║██╔════╝██║  ██║    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║███████╗███████║    ███████║███████║██║     █████╔╝ █████╗  ██████╔╝
██║╚════██║██╔══██║    ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║███████║██║  ██║    ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                       



          {Wh}[ + ]  C O D E   B Y  M A R S X  [ + ]  
        
    {Wh}[ 1 ] {Gr}IP Tracker
    {Wh}[ 2 ] {Gr}Hacked Cameras
    {Wh}[ 4 ] {Gr}WebHook Spam
    {Wh}[ 0 ] {Gr}Exit
""")

input_user = input(f'\n   {Wh}@ISH-HACKER😎~# {Gr}')


if input_user == '1': #OPSI 1
    os.system('clear')
    time.sleep(1)
    stderr.writelines(f"""{Wh}
     
      {Wh}----------------------------------
      {Wh}| {Gr}ISH - HACKER - IP ADDRESS      {Wh}|
      {Wh}|        {Gr}@CODE BY MARSX          {Wh}|
      {Wh}----------------------------------


___________                     __           
\__    ___/___________    ____ |  | _____.__.
  |    |  \_  __ \__  \ _/ ___\|  |/ <   |  |
  |    |   |  | \// __ \\  \___|    < \___   |
  |____|   |__|  (____  /\___  >__|_ \/ ____|
                      \/     \/     \/\/     
   
    """)

    try:
        def IP_Track():
            ip = input(f"{Wh}\n Enter IP target : {Gr}")
            print()
            print(f' {Wh}============= {Gr}SHOW INFORMATION IP ADDRESS {Wh}=============')
            req_api = requests.get(f"http://ipwho.is/{ip}")
            ip_data = json.loads(req_api.text)
            time.sleep(2)
            print(f"{Wh}\n IP target       :{Gr}", ip)
            print(f"{Wh} Type IP         :{Gr}", ip_data["type"])
            print(f"{Wh} Country         :{Gr}", ip_data["country"])
            print(f"{Wh} Country Code    :{Gr}", ip_data["country_code"])
            print(f"{Wh} City            :{Gr}", ip_data["city"])
            print(f"{Wh} Continent       :{Gr}", ip_data["continent"])
            print(f"{Wh} Continent Code  :{Gr}", ip_data["continent_code"])
            print(f"{Wh} Region          :{Gr}", ip_data["region"])
            print(f"{Wh} Region Code     :{Gr}", ip_data["region_code"])
            print(f"{Wh} Latitude        :{Gr}", ip_data["latitude"])
            print(f"{Wh} Longitude       :{Gr}", ip_data["longitude"])
            lat = int(ip_data['latitude'])
            lon = int(ip_data['longitude'])
            print(f"{Wh} Maps            :{Gr}",f"https://www.google.com/maps/@{lat},{lon},8z")
            print(f"{Wh} EU              :{Gr}", ip_data["is_eu"])
            print(f"{Wh} Postal          :{Gr}", ip_data["postal"])
            print(f"{Wh} Calling Code    :{Gr}", ip_data["calling_code"])
            print(f"{Wh} Capital         :{Gr}", ip_data["capital"])
            print(f"{Wh} Borders         :{Gr}", ip_data["borders"])
            print(f"{Wh} Country Flag    :{Gr}", ip_data["flag"]["emoji"])
            print(f"{Wh} ASN             :{Gr}", ip_data["connection"]["asn"])
            print(f"{Wh} ORG             :{Gr}", ip_data["connection"]["org"])
            print(f"{Wh} ISP             :{Gr}", ip_data["connection"]["isp"])
            print(f"{Wh} Domain          :{Gr}", ip_data["connection"]["domain"])
            print(f"{Wh} ID              :{Gr}", ip_data["timezone"]["id"])
            print(f"{Wh} ABBR            :{Gr}", ip_data["timezone"]["abbr"])
            print(f"{Wh} DST             :{Gr}", ip_data["timezone"]["is_dst"])
            print(f"{Wh} Offset          :{Gr}", ip_data["timezone"]["offset"])
            print(f"{Wh} UTC             :{Gr}", ip_data["timezone"]["utc"])
            print(f"{Wh} Current Time    :{Gr}", ip_data["timezone"]["current_time"])
        if __name__ == '__main__':
            IP_Track()
    except KeyboardInterrupt:
        print(f" {Wh}[{Ye}!{Wh}] {Ye}PROGRAM STOPPED...")


elif input_user == '2':  
    os.system('clear')
    time.sleep(1)
    stderr.writelines(f"""{Wh}

      {Wh}----------------------------------
      {Wh}| {Gr}ISH - HACKER - HACKED CAMERAS  {Wh}|
      {Wh}|        {Gr}@CODE BY MARSX          {Wh}|
      {Wh}----------------------------------

    """)

    try:
       
        data_folder_path = 'data'
        cam_hackers_path = os.path.join(data_folder_path, 'cam-hackers.py')

       
        os.system(f'python {cam_hackers_path}')

    except Exception as e:
        print(f" {Wh}[{Ye}!{Wh}] {Ye}An error occurred: {e}")


elif input_user == '3':
    os.system('clear') 
    time.sleep(1)
    stderr.writelines(f"""{Wh}

      {Wh}----------------------------------
      {Wh}|     {Gr}ISH - HACKER - WebHook     {Wh}|
      {Wh}|        {Gr}@CODE BY MARSX          {Wh}|
      {Wh}----------------------------------

    """)

    try:
       
        data_folder_path = 'data'
        cam_hackers_path = os.path.join(data_folder_path, 'WebhookSpam.py')

       
        os.system(f'python {cam_hackers_path}')

    except Exception as e:
        print(f" {Wh}[{Ye}!{Wh}] {Ye}An error occurred: {e}")

elif input_user == '0':
    print(f"\n  {Wh}[{Ye}!{Wh}] {Ye}THANK'S FOR USING TOOL {Ye}ISH-HACKER !")
else:
    print(f" {Ye}Opss no option !") 
