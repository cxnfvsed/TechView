#!/usr/bin/env python3

import rospy
import cv2

from ROSCommunicator.messageProc import *

class Image_processing:

    GREEN = (0, 255, 0)
    RED = (0, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    person_count = 0


    def Focal_Length_Finder(measured_distance, real_width, width_in_rf_image):
        # finding the focal length
        focal_length = (width_in_rf_image * measured_distance) / real_width
        return focal_length


    def Distance_finder(Focal_Length, real_face_width, face_width_in_frame):
        distance = (real_face_width * Focal_Length) / face_width_in_frame

        return distance


    def face_data(image):
        global person_count
        face_width = 0  
        face_detector = cv2.CascadeClassifier("/home/cxnfused/catkin_ws/src/TechView/src/Resources/haarcascade_frontalface_default.xml")

        if face_detector == None:
            print("[TechView] no model loaded")
            #msg = "no model"
            #Sender.send(topic_name='CU_name',String=String,queue_size=10,signal=msg)
            
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray_image, 1.3, 5)

        #print ("faces: " + str(faces) + str(type(faces)))
        
        if len(faces) != 0:
            cv2.putText(image, "person number: " + str(len(faces)), (470, 85), cv2.FONT_HERSHEY_SIMPLEX, 0.6, Image_processing.GREEN, 2)
            person_count=len(faces)
            msg = f"FACES_NUMBER:{person_count}"
            Sender.send(topic_name='tech_view',signal=msg)
        for (x, y, h, w) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), Image_processing.GREEN, 2)
            face_width=w
        return face_width
