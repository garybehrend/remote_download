'''
Program to create a file containing info for download

File:   extension: .download
        firstline: url of file to download

Author: Phil McCredden
Date:   October 19, 2015
'''

import os
from urllib.request import urlopen


# Test the url to see if valid
def test_url(url):
    try:
        urlopen(url)
        return True
    except IOError:
        return False

# Get url from user and check if valid
print('Remote url downloader using dropbox @action')
url = input('Enter url to download (q=quit): ')
if url == 'q':
    exit()
url_check = test_url(url)
if url_check:
    print('added to download queue ...')
else:
    print('Url is invalid!')

# Output the file into dropbox
output_path = os.path.expanduser('~/Dropbox/@Action/test.dwn')
output_file = open(output_path, 'w')
output_file.writelines(url)
output_file.close()
