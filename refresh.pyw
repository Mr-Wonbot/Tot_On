from __future__ import unicode_literals
import time
from datetime import datetime as dt

#hard coded parameters

host_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
black_list = ["www.facebook.com","www.youtube.com"]


while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 0) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 4):
        print("Time block reserved for work")
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in black_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in black_list):
                    file.write(line)
            file.truncate()
        print("Free time")
    time.sleep(5)


