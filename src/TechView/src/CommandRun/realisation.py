#!/usr/bin/env python

import cv2

#from potok import WebcamStream

class commandExec:

    changes = False

    def changeRes(cap,data):
        height,width = data.split(",")
        #WebcamStream.set(WebcamStream,height,width)
        cap.set(3,int(height))
        cap.set(4,int(width))
        cap.open(0)
        print(f"[Resolution] resolution set to {height}x{width}")

    def changeFrameRate(cap, data):
        cap.set(5, int(data))
        print(f"[frameRate] frame rate set to {data}")

    def camMode(cap, data):
        if int(data) == 1:
            print("[camMode] ON")
        elif int(data) == 0:
            cap.release()
            cv2.destroyAllWindows()
            print("[camMode] OFF")
        else:
            print("[camMode] incorrect value")

    def changeDistance(data):
        print(f"[changeDst] distance set to {data}")

        return int(data)
    
    def comHelp():
        print("[commands]\n ChangeRes x,y - change camera resolution\n setFrameRate x - change camera frame rate\n changeDst x - change distance to object")