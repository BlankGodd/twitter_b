#usr/bin/python
# Author:   @BlankGodd_

import getpass
from platform import system
import os, shutil

class FileError(Exception):
	pass

def add_for_windows(user,script_file):
    bat = r"C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" % user
    shutil.copy2(script_file, bat)
    # for pc that opens up script instad of running
    with open(bat+'\\'+"open.bat","w+") as bat_file:
        bat_file.write(r'python %s' % script_file)
        
def add_for_linux():
    print("Go and use cron jobs")

if __name__ == "__main__":
    opsys = system()
    if opsys == "Windows":
        try:
            user = getpass.getuser()
            script_file = input("Enter file path: ")
            add_for_windows(user,script_file)
            print("File added")
        except:
            raise FileError("Could not add file to autorun!")
    if opsys == "Linux":
        pass

        
