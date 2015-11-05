#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
"""
Program launched from Hazel
Open txt file and download the filename stored
in first line.
This allows to sync the folder via dropbox and
add files to be downloaded on a remote computer.
Accompaning program - add_download.py

Author: Phil McCredden
Date:   October 19, 2015

"""

import sys
import os
import logging
import datetime
import json
import smtplib
open requests


class EmailProfile:

    def __init__(self):
        """check to see if it exists if not write a template file"""
        config_file = "config.json"

        try:
            # Lets see if the config file exists
            with open(config_file) as json_data_file:
                # the config file exists so setup variables
                data = json.load(json_data_file)
                self.smtp_server = data["email"]["smtp_server"]
                self.smtp_port = data["email"]["smtp_port"]
                self.email_from = data["email"]["email_address"]
                self.email_password = data["email"]["email_password"]
                self.email_to = data["email"]["email_to"]
                self.email_subject = data["email"]["email_subject"]
        except IOError:
            # config file does not exist,
            print('config.json file does not exist.\n'
                  'Default created please edit details')
            # so create it
            data = {
                "email": {
                    "smtp_server": "smtp.gmail.com",
                    "smtp_port": "587",
                    "email_from": "email@address",
                    "email_password": "xxxx",
                    "email_to": "email@address",
                    "email_subject": "Remote Download Notification"
                },
                "other": {
                    "future": "blah"
                }
            }
            with open(config_file, 'w') as outfile:
                json.dump(data, outfile)
                exit()


def log(prog_name, log_action):
    """log function - prog_name will be used to create the log file
    in the format of prog_name.log as well as storing it in the log itself.
    The log_action should be set to either start or finish and the Date
    and time will be logged"""

    file_name = prog_name + '.log'
    logging.basicConfig(filename=file_name, level=logging.DEBUG)
    local_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
    logging.info(local_time + ' : ' + prog_name + ' : ' + log_action)

prog_name = 'remote_download'  # set logging var

hazel_infile = sys.argv[1]  # read name of file to download
array = []
with open(hazel_infile, "r") as f:
    for line in f:
        array.append(line)

# get variables from file
url = array[0]
saved_name = array[1]

# Formulate path and file name to save
saved_path = os.path.expanduser('~/hazel_downloads/')
saved_fullpath = os.path.join(saved_path, saved_name)

log(prog_name, 'start')  # Log start time

r = requests.get(url)
with open(saved_fullpath, "wb") as code:
    code.write(r.content)

log(prog_name, 'finish')  # Log end time

""" send email to user notifying of completion"""
em = EmailProfile()
current_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
email_subject = 'Remote Download Notification'
email_content = '%s downloaded at %s' % (saved_name, current_time)
email_message = 'Subject: %s\n\n%s' % (email_subject, email_content)

# send the email using the smtp library
mail = smtplib.SMTP(em.smtp_server, em.smtp_port)
mail.ehlo()
mail.starttls()
mail.login(em.email_from, em.email_password)
mail.sendmail(em.email_from, em.email_to, email_message)
mail.close()
