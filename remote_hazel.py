#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
'''
Program launched from Hazel
Open txt file and download the filename stored
in first line.
This allows to sync the folder via dropbox and
add files to be downloaded on a remote computer.
Accompaning program - add_download.py

Author: Phil McCredden
Date:   October 19, 2015

'''

import sys
import urllib.request
import os
import logging
import datetime


def log(prog_name, log_action):
    """log function - prog_name will be used to create the log file
    in the format of prog_name.log as well as storing it in the log itself.
    The log_action should be set to either start or finish and the Date
    and time will be logged"""

    file_name = prog_name + '.log'
    logging.basicConfig(filename=file_name, level=logging.DEBUG)
    today = datetime.date.today()
    local_time = today.ctime()
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
urllib.request.urlretrieve(url, saved_fullpath)  # Write to file
log(prog_name, 'finish')  # Log end time
