'''
Program to create a file containing info for download

File:   extension: .download
        firstline: url of file to download

Author: Phil McCredden
Date:   October 19, 2015
'''

import os
from urllib.request import urlopen
import time


# Test the url to see if valid
def test_url(url):
    try:
        urlopen(url)
        return True
    except IOError:
        return False


# Get url from user and check if valid
def input_url():
    print('Remote url downloader using dropbox @action')
    url = input('Enter url to download (q=quit): ')
    if url == 'q':
        exit()
    url_check = test_url(url)
    if url_check:
        pass
    else:
        print('Url is invalid!')
    return url


# add a input for the saved name
def input_savedname():
    saved_file = input('Enter the name you would like to save the file as: ')
    return saved_file


# Output the file into dropbox
def output_file(url, saved_filename):
    output_extension = '.dwn'
    prefix_name = 'Remote Download | '
    date_stamp = time.strftime("%H:%M:%S")
    output_file = prefix_name + date_stamp + output_extension
    output_path = os.path.expanduser('~/Dropbox/@Action/')
    output_path = output_path + output_file + output_extension
    output_file = open(output_path, 'w')
    print('url is ' + url)
    print('saved_filename ' + saved_filename)
    output_file.writelines([url, '\n', saved_filename])
    output_file.close()
    print('added to download queue ...')
    return


# Main function
def main():
    url = input_url()
    saved_filename = input_savedname()
    output_file(url, saved_filename)

if __name__ == "__main__":
    main()
