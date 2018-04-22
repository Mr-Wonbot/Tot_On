from __future__ import unicode_literals
import time
from datetime import datetime as dt
from prompt_toolkit import prompt

host_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
black_list = []
site = ""
start_time = 0
end_time = 0
while(site != "done"):
    start_time = prompt("What time would you like to start the blocking session?\n")
    end_time = prompt("What time would you like to end the blocking session?\n")
    site = prompt("Enter a url(s) you'd like to add to the blacklist(end input: done):\n")
    if (site == "done"):
        break;
    black_list.append("www."+site+".com")

print(black_list)

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, start_time) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end_time):
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


