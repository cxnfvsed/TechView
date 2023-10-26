#!/usr/bin/env python
import rospy
from std_msgs import String
from ROSCommunicator.messageProc import *

class External_signals:
    setAutopilot = True
    systemStatus = True

    ApTopic = '/path'
    CuTopic = '/path1'
    DcTopic = '/path2'

    def sendToAutopilot(signal):

        if External_signals.setAutopilot == True:
            print(f"[autopilot] {signal}")
            Sender.send(topic_name=External_signals.ApTopic,String=String,queue_size=10,signal=signal)
        elif External_signals.setAutopilot == False:
            print(f"[autopilot] {signal}")
            Sender.send(topic_name=External_signals.ApTopic,String=String,queue_size=10,signal=signal)
        else:
            print("[APSingnal] incorrect format.")
        

    def sendSystemStatusCU(signal):
        if External_signals.systemStatus == True:
            print(f"[CU] status: {signal}")
            Sender.send(topic_name=External_signals.ApTopic,String=String,queue_size=10,signal=signal)
        else:
            print(f"[CU] status: {signal}")
            Sender.send(topic_name=External_signals.ApTopic,String=String,queue_size=10,signal=signal)
        

    def sendSystemStatusDU(signal):
        if External_signals.systemStatus == True:
            print(f"[DU] status: {signal}")
            Sender.send(topic_name=External_signals.ApTopic,String=String,queue_size=10,signal=signal)
        else:
            print(f"[DU] status: {signal}")
            Sender.send(topic_name=External_signals.ApTopic,String=String,queue_size=10,signal=signal)


    def formAutopilotSignal(data):
        state = int(data)
        sigOn = "OK"
        sigOff = "person to close"
        if state == 1:
            External_signals.setAutopilot = True
            return sigOn
        if state == 0:
            External_signals.setAutopilot = False
            return sigOff
            

    def formSystemSignal(data):
        state = int(data)
        msg = "[camera] stable work"
        msg2 = "[camera] error occured"
        if state == 1:
            # print("[system] works fine")
            External_signals.systemStatus = True
            return msg
        elif state == 0:
            #print("[system] offline")
            External_signals.systemStatus = False
            return msg2