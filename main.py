import os
import sys
import time

# Type of Error using an Integer.
error_type = 0

# Directories and File Types
CWD = os.getcwd()
COMMANDSDIR = CWD + "\\commands\\"
ERRORDIR = CWD + "\\errors\\"
HLPDIR = COMMANDSDIR + "\\help\\"
TXT = ".txt"

# Files
WELCOME = open((COMMANDSDIR + "Welcome" + TXT), "r").read()
NAN = open((ERRORDIR + "NaN" + TXT), "r").read()
NAC = open((ERRORDIR + "NaC" + TXT), "r").read()
FNF = open((ERRORDIR + "FNF" + TXT), "r").read()
README = open("README.md", "r").read()
LICENSE = open("LICENSE", "r").read()

# Help Information
hlp_Copy = open((HLPDIR + "Copy.txt"))

# Commands
LSDR = open((COMMANDSDIR + "ListDir.py"), "r")
CPY = open((COMMANDSDIR + "Copy.py"), "r")

print("""\033[32m
            Welcome!
      Choose your command!\033[97m
      """)

time.sleep(1)

# Input and Reset after an Error Occurs.
_input = input(">> ")

def reset_input():
    _input = input(">> ")

if(_input == "cli"):
    print(WELCOME)

if(_input == "" or _input == " "):
    error_type = 1
    if(error_type == 1):
        reset_input()

# If "Exit" or "Quit" is entered into the console then exit the program.
if(_input == "exit" or _input == "quit"):
    print("Exiting OpenCLI.")
    time.sleep(0.3)
    print("Bye " + os.environ["USERNAME"] + ".")
    sys.exit(1)

# List Directory
if(_input == "ls" or _input == "dir"):
    os.startfile(LSDR)

# Errors
#   |--> 1. NaC = Not a Command.
#   |--> 2. NaN = Not a Number.
#   |--> 3. FnF = File not Found.
if(error_type == 1):
    print("\033[31m" + NAC + "\033[97m")
if(error_type == 2):
    print("\033[31m" + NAN + "\033[97m")
if(error_type == 3):
    print("\033[31m" + FNF + "\033[97m")

# Important Files
if(_input == "README.md"):
    print("\n" + README)
    reset_input()
if(_input == "LICENSE"):
    print("\n" + LICENSE)
    reset_input()

# Help Info
if(_input == "copy -h" or _input == "copy -help"):
    print("\n" + hlp_Copy)
