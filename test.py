from twilio.rest import Client
import serial
import time
import os
import threading
import config

#Twilio API

client = Client(config.twKey, config.twToken)

def getMotion():
    ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
    ser.flush()
    while True:
        try:
            motion = ser.readline().decode('utf-8').rstrip()
            motion = int(motion)
        except:
            continue
        break
    return motion

def motionPrint():
    while True:
        sleepTime()
        motion = getMotion()
        if motion == 1:
            message = "Motion has been detected!"
        elif motion == 0:
            message = "No motion has been detected."
    return print(message)

def sleepTime():
    time.sleep(1)

def textTimer():
    time.sleep(3600)

def motionMonitor():
    while True:
        sleepTime()
        motion = getMotion()

        if motion == 1:

        # Print message in the terminal for reference
            message = "Motion has been detected!"
            # Txt notification
            txt_message = client.messages \
                .create(
                body=message,
                from_='+14792028274',
                to='+12102029621'
            )
            print(txt_message.sid)

            txt_message = client.messages \
                .create(
                body=message,
                from_='+14792028274',
                to='+12106877697'
            )
            print(txt_message.sid)

            os.system("mpg123 " + "goodbye.mp3")

            textTimer()

def testing():
    while True:
        sleepTime()
        ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
        ser.flush()

        motion = ser.readline().decode('utf-8').rstrip()
        print(motion)

if __name__ == '__main__':
    #motionThread = threading.Thread(target=motionMonitor)
    #printThread = threading.Thread(target=motionPrint)

    #motionThread.start()
    #printThread.start()

    testing()
