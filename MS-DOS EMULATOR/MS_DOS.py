import time
import os
import shutil


from datetime import datetime
def DEBUG_MODE_BOOT():
    
    DEBUG_MODE = input("Would you like to boot in debug mode? (Y/N) ")
    if DEBUG_MODE == "Y":
        def init():
            print("DEBUG_MODE ACTIVE")

            print("INITIALIZING RAM...")
            time.sleep(0 or 1)
            print("Done")
            time.sleep(1 or 2)
            print("INITIALIZING CPU...")
            time.sleep(0 or 1)
            print("Done")
            time.sleep(2 or 3)
            print("SYNCING CLOCK...")
            time.sleep(1)
            print("Done")
            print("INITIALIZING Local Disk...")
            time.sleep(0 or 2)
            print("Done")
            print("VERIFYING DRIVE INTEGRITY...")
            time.sleep(0 or 3)
            print("Done")
            time.sleep(1 or 4 or 2)
            print("BIOS VER: 1.0")
            print("CPU: Generic 486 MHz CPU")
            print("RAM: 16 MB 100 MHz RAM Module")
            print("Local Disk: Lbl='C:' size='1 GB'")
            print("Starting MS-DOS...")
            time.sleep(0 or 10)
            print("Done")
        init()
    if DEBUG_MODE == "N":
        print("Starting MS-DOS...")
        print("Type 'help' for a list of commands and more information")
        def TERMINAL():
            now = datetime.now()

            current_time = now.strftime("%H:%M:%S")
            
            drive = 1
            drivelbl = "C:"
            if drive == 1:
                drivelbl == "C:"
            if drive == 2:
                drivelbl == "A:"
            
            command = input(drivelbl + "\>")
            if command == "dir":
                print(drivelbl + """\

            \DOS""")
            if command == "cls":
                print(("""
        """) * 40)
            if command == "A:":
                drive = 2
                print("This functionality is unavaliable right now.")
            if command == "shutdown":
                exit()
            if command == "cd DOS":
                print("This functionality is unavaliable right now.")
            if command == "help":
                os.system("start Info.txt")
            if command == "say":
                say = input("What would you like to say? ")
                print(say)
            if command == "ver":
                print("MS-DOS Emulator version 0.1.0")
            if command == "time":
                print(current_time)

            if command == "cmd":
                os.system("start cmd.exe")
            if command == "restart":
                resAsk = input("Are you sure you want to restart the shell? (Y/N) ")
                if resAsk == "Y":
                    print("Restarting Shell...")
                    time.sleep(1 or 3)
                    print(("""
            """) * 40)
                    TERMINAL()
                if resAsk == "N":
                    TERMINAL()
            if command == "restartdb":
                resDBAsk = input("Are you sure you want to restart the shell in debug mode? (Y/N) ")
                if resDBAsk == "Y":
                    print("Restarting Shell in DEBUG mode...")
                    time.sleep(1 or 3)
                    print(("""
            """) * 40)
                    DEBUG_MODE_BOOT()
                if resDBAsk == "N":
                    TERMINAL()
            if command == "createFile":
                fileName = input("Type the file name and extension (Ex: text.txt): ")
                try:
                    os.system("cd ./Created_Files")
                    f = open(fileName,"w+")
                    f.close()
                    original = fileName
                    target = "./Created_Files"

                    shutil.move(original,target)
                     
                except():
                    print("File Creation failed!")
            if command == "viewFile":
                filetoopen = input("Please enter the filename and extension (Ex: Text.txt): ")
                try:
                    os.system("cd ./Created_Files")
                    os.system("start " + filetoopen)
                except():
                    filenotfound = input("The file you requested could not be found. Would you like to create it instead? (Y/N) ")
            if command == "moveFile":
                original = input("Please enter the file name: ")
                target = input("Directory to move to: ")
                try:
                    shutil.move(original,target)
                except():
                    print("An error occured while moving the file.")

            
            TERMINAL()
        TERMINAL()
    def DEBUG_TERMINAL():
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        
        drive = 1
        drivelbl = "C:"
        if drive == 1:
            drivelbl == "C:"
        if drive == 2:
            drivelbl == "A:"
        
        command = input(drivelbl + "\>")
        if command == "dir":
            print(drivelbl + """\

        \DOS""")
        if command == "cls":
            print(("""
    """) * 40)
        if command == "A:":
            drive = 2
            print("This functionality is unavaliable right now.")
        if command == "shutdown":
            exit()
        if command == "cd DOS":
            print("This functionality is unavaliable right now.")
        if command == "help":
            os.system("start Info.txt")
        if command == "say":
            say = input("What would you like to say? ")
            print(say)
        if command == "ver":
            print("MS-DOS Emulator version 0.1.0")
        if command == "time":
            print(current_time)

        if command == "cmd":
            os.system("start cmd.exe")
        if command == "restart":
            print("Restarting Shell...")
            time.sleep(1 or 3)
            print(("""
    """) * 40)
            init()

            
        DEBUG_TERMINAL()
DEBUG_MODE_BOOT()
DEBUG_TERMINAL()
init()    
TERMINAL()

