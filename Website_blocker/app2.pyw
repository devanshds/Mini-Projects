"""This app enables its user to block access to any of the websites at any particular time of the day"""
#run this program as administrator
import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"   #r is prefixed for raw string
redirect="127.0.0.1"
website_list=["fb.com","facebook.com","www.facebook.com","www.fb.com"] #list of websites to block

while True:
    if dt( dt.now().year,dt.now().month,dt.now().day,8 ) < dt.now() < dt( dt.now().year,dt.now().month,dt.now().day,16 ):  #change the time as per your requirements
        print("Working hours..." )  #text to confirm working
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n" + redirect + " " + website)
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in content for website in website_list):
                    file.write(line)
                file.truncate()
        print("Fun hours...")
    time.sleep(10)  # repeats while loop every 10 seconds
