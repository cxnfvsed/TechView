#!/usr/bin/env python3

import cv2
import socket
import numpy as np
import pickle
import rospy

from ImageProcessing.procis import Image_processing
from ROSCommunicator.messageProc import *

rospy.init_node("server", anonymous=True)

ip = "192.168.43.211"
port = 60000

known_distance = 96
known_width = 14
frame_counter = 0
sysState = 1 

GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLACK = (0, 0, 0)
fonts = cv2.FONT_HERSHEY_COMPLEX

ref_image = cv2.imread("/home/cxnfused/catkin_ws/src/TechView/src/Resources/ref.png")
face_width_img = Image_processing.face_data(ref_image)
focal_length = Image_processing.Focal_Length_Finder(known_distance,known_width,face_width_img)
#cv2.imshow("ref image",ref_image)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((ip,port))

print("[server] binded")
while True:
    x = s.recvfrom(1000000)
    clientip = x[1][0]
    data = x[0]
    data = pickle.loads(data)
    data = cv2.imdecode(data,cv2.IMREAD_COLOR)
    frame_counter += 1

    face_width_frame = Image_processing.face_data(data)
    if face_width_frame != 0:
        distance = Image_processing.Distance_finder(focal_length,known_width,face_width_frame)

        dm= f"DISTANCE:{round(distance, 2)} cm"
        Sender.send(topic_name='tech_view',signal=dm)

        cv2.line(data, (30, 30), (230, 30), RED, 32)
        cv2.line(data, (30, 30), (230, 30), BLACK, 28)
        cv2.putText(data, f"Distance: {round(distance, 2)} CM", (30, 35),fonts, 0.6, GREEN, 2)

        APm = "turning off autopilot"

        if distance < 100:
            msg = f"CRITICAL_WARNING:{APm}"
            Sender.send(topic_name='tech_view',signal=msg)
        
    cv2.imshow("[stream]",data)

    if cv2.waitKey(10) == ord("q"):
        break

cv2.destroyAllWindows()
s.close()


