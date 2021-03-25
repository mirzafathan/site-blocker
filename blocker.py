import time
from datetime import datetime as dt


hosts_path = "/etc/hosts"
redirect = "127.0.0.1"


website_list = []

while True:
    print("Working hours...")
    with open(hosts_path, 'r+') as file:
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                file.write(redirect + " " + website + "\n")
    time.sleep(5)
