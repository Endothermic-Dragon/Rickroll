import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from data_extract import playsound

loc = "data1.wav"

with open("data.bin", "rb") as dataFile:
    data = dataFile.read()

with open(loc, "wb") as data1:
    data1.write(data)

playsound(loc)

# https://development-tools.net/python-obfuscator/

# Windows - https://github.com/AndreMiras/pycaw
# Above from https://stackoverflow.com/questions/20828752/python-change-master-application-volume
# Mac - https://stackoverflow.com/questions/2565204/adjust-osx-system-audio-volume-in-python
# Linux - https://stackoverflow.com/questions/8220108/how-do-i-check-the-operating-system-in-python