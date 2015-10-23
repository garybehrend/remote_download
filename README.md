# remote_download
Download files on another mac using a hazel rule and two python programs.

I used this program to learn python, so I am sure I have not done it the most professional or efficient way
but it works, so I am happy.

Happy to receive comments and feedback regarding improvements.

##Requirements:##

1. Mac
2. Hazel (https://www.noodlesoft.com/hazel.php)
3. Dropbox (http://www.dropbox.com)
4. Python 3

##Todo:##

1. ~~Create a logging process - start time and finish time.~~
2. Notification process - sms, email or twitter.
3. Implement a config file using json (for mail settings etc)
3. Add a gui interface

##Setup:##

1. On the computers that you wish to remotely set up the downloads you need
to install dropbox (and create a @action folder). In addition have the
remote_download.py file to run the program.

2. On server computer also install dropbox. In addition, install hazel.

3. Create a hazel rule to monitor the ~/Dropbox/@Action folder for files
with an extension of '.dwn' and no tag color of green. This rule when it finds ones, set the tag color to green and initialises the shell command. Set your shell environment to the path of python3. In the shell script put the contents
of remote_hazel.py
