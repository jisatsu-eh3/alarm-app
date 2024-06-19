from twilio.rest import Client
import serial
import time
import os
#import threading
#import config
#from picamera import PiCamera
from datetime import datetime
import random

#Twilio API
#client = Client(config.twKey, config.twToken)

#camera = PiCamera()

def getSoundClips():
    path = "/home/ubuntu/alarm_project/sound_clips/"
    soundClips = os.listdir(path)
    clip = random.choice(soundClips)
    fullClip = path + clip

    return print(fullClip)

def getMotion(clip):
    clip = "omxplayer " + clip
    ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
    ser.setDTR(False)
    sleepTime()
    ser.flushInput()
    ser.setDTR(True)
    with ser:
        while True:
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            motion = ser.readline().decode('utf-8').rstrip()
            motion = str(motion)
            print(motion)

            if motion == '1':

                # Print message in the terminal for reference
                #message = "Motion has been detected!"
                # Txt notification
                #txt_message = client.messages \
                #    .create(
                #    body=message,
                #    from_='+14792028274',
                #    to='+12102029621'
                #)
                #print(txt_message.sid)

                #txt_message = client.messages \
                #    .create(
                #    body=message,
                #    from_='+14792028274',
                #    to='+12106877697'
                #)
                #print(txt_message.sid)

                os.system(clip)
                #camera.capture("/home/xoxoiindy/motionSensor/captures/" + dt_string + '_capture.jpg')

                textTimer()

    return

def motionPrint():
    while True:
        time.sleep(1)
        motion = getMotion()
        if motion == '1':
            message = "Motion has been detected!"
        elif motion == '0':
            message = "No motion has been detected."
    return print(message)

def sleepTime():
    time.sleep(1)

def textTimer():
    time.sleep(60)

def motionMonitor():
    while True:
        sleepTime()
        motion = getMotion()
        print(type(motion))
        print(motion)

        if motion == '1':

        # Print message in the terminal for reference
            #message = "Motion has been detected!"
            # Txt notification
            #txt_message = client.messages \
            #    .create(
            #    body=message,
            #    from_='+14792028274',
            #    to='+cell'
            #)
            #print(txt_message.sid)

            #txt_message = client.messages \
            #    .create(
            #    body=message,
            #    from_='+14792028274',
            #    to='+cell'
            #)
            #print(txt_message.sid)

            os.system("mpg123" + "goodbye.mp3")
            print("Played audio")

            textTimer()

        else:
            print(motion)
            sleepTime()

if __name__ == '__main__':
    #motionThread = threading.Thread(target=motionMonitor)
    #printThread = threading.Thread(target=motionPrint)

    #printThread.start()
    #motionThread.start()
    #getMotion()
    getSoundClips()
    getMotion()
