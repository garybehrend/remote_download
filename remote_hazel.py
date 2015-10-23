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
import time

# read name of file to download
hazel_infile = sys.argv[1]
file_name = open(hazel_infile, 'r')
first_line = file_name.readline()

# get variables from file
input_file = hazel_infile.read()
url = input_file.splitlines()[0]
saved_name = input_file.splitlines()[1]

# Formulate path and file name to save
saved_path = os.path.expanduser('~/hazel_downloads')
saved_fullpath = os.path.join(saved_path, saved_name)

# Set up logging variables
logging.basicConfig(filename='remote_download.log', level=logging.DEBUG)
prog_name = 'remote_download'

# Log start time
localtime = time.asctime(time.localtime(time.time()))
log_action = 'start'
logging.info(localtime + ' : ' + prog_name + ' : ' + log_action)

# Write to log file
urllib.request.urlretrieve(url, saved_fullpath)

# Log end time
log_action = 'finish'
localtime = time.asctime(time.localtime(time.time()))
logging.info(localtime + ' : ' + prog_name + ' : ' + log_action)
