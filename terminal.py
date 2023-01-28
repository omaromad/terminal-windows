import subprocess
import pyfiglet
import time
from colorama import Fore
import sys
import os
#end_result = "<end_of_result>"
stx = (Fore.WHITE)
text = pyfiglet.figlet_format("terminal x-1")
print( stx ,text)
while True:
    try:

        #command = input ("root"+Fore.RED+"@"+Fore.WHITE+ "hacker>")
        #if command.lower() ==  "exit":
        #    break

        output = subprocess.run(["powershell", "netstat"],shell=True,capture_output=True)
        print (output)
    except Exception:
        time.sleep(5)
        print("________________________________")
        continue
