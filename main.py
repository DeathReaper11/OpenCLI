import os
import sys
import time

# Type of Error using an Integer.
error_type = 0

# Directories and File Types
CWD = os.getcwd()
COMMANDSDIR = CWD + "\\commands\\"
ERRORDIR = CWD + "\\errors\\"
TXT = ".txt"

# Files
WELCOME = open((COMMANDSDIR + "Welcome" + TXT)).read()
NAN = open((ERRORDIR + "NaN" + TXT)).read()
NAC = open((ERRORDIR + "NaC" + TXT)).read()

print("""
      Welcome!
      Choose your command!
      """)

time.sleep(1)
_input = input(">> ")

if(_input == "cli"):
    print(WELCOME)

if(_input == "" or _input == " "):
    error_type = 1
    #time.sleep(1.0)
    #error_type = 0

if(_input == "exit" or _input == "quit"):
    print("Exiting OpenCLI.")
    time.sleep(0.5)
    print("Bye " + os.environ["USERNAME"])
    sys.exit(1)

# Errors
    # 0. Nan = Not a Number.
    # 1. NaC = Not a Command.
if(error_type == 1):
    print(NAC)