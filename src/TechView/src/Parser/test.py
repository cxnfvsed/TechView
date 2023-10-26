#!/usr/bin/env python


from CommandRun.realisation import commandExec
import cv2

class ParseIncome:

    def parseCommand (vid,command):
    
        args = command.split(" ")
        print(f"recieved {args}")

        if args[1] == "changeRes":
            commandExec.changeRes(vid,args[2])
        elif args[1] == "setFrameRate":
            commandExec.changeFrameRate(vid,args[2])
        elif args[1] == "cam":
            commandExec.camMode(vid,args[2])
        elif args[1] == "changeDst":
            commandExec.changeDistance(args[2])
        elif args[1] == "help":
            commandExec.comHelp()
        else:
            print("no such command")
