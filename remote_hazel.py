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

# read name of file to download
hazel_infile = sys.argv[1]
file_name = open(hazel_infile, 'r')
first_line = file_name.readline()

# Download the file from `url`
url = first_line

saved_path = os.path.expanduser('~/hazel_downloads')

# want to find final file name
find_param = first_line.rfind('/')
start_pos = find_param + 1
end_pos = len(first_line)
last_phrase = first_line[start_pos:end_pos]

saved_fullpath = os.path.join(saved_path, last_phrase)
print("saved_path = " + saved_fullpath)
print("url = " + url)

urllib.request.urlretrieve(url, saved_fullpath)
