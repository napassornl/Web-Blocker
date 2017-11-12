# Make this program run whe computer starts using Cron service
    # sudo crontab -e

import time
from datetime import datetime as dt
# import datetime class in datatime module as dt namespace

hosts_path = "hosts" #if test script, need to open command line as admin
# do by adding sudo python3 website_blocker.py
hosts_temp = "hosts" # should make a copy of host file, if there is an error in script
redirect = "127.0.0.1" # IP address of websites that want to block
website_list =["www.facebook.com", "facebook.com"]

while True: # during certain period of time, the website list will be written in
# the hosts file, so they will be block, so you cannot play them during that time,
# script runs the whole time
    if dt(dt.now().year, dt.now().month, dt.now().day, 11) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        # dt.now().year returns an integer of the current year. month, etc
        # dt.now() and dt(...) creates a data time object
        print("Working hours... ")
        with open(hosts_path,"r+") as file: # can read and append**
            content = file.read()
            # append the websites to teh hosts file
            for website in website_list:
                if website in content:
                    pass # goes to sleep for 5 seconds
                else:
                    file.write(redirect + " " + website + "\n") # at least one space
                    # is required between the redirect and website
    else:
        # want to delete the websites from teh hosts file - no direct way to delete
        print("Fun hours...")
        with open(hosts_path,"r+") as file: # can read and append**
            content = file.readlines() # produces a lists with all the lines in hosts
            # pointer will be placed at the last line
            file.seek(0) # places pointer in front of first character of file content
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line) # append line to hosts after the pointer
            file.truncate() # removes the content after the pointer which is the old content

    time.sleep(5) # waits every 5 sec before exiting the loop
