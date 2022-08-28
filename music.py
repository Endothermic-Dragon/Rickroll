import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from data_extract import playsound

loc = "data.wav"

with open("data.bin", "rb") as dataFile:
    data = dataFile.read()

with open(loc, "wb") as data1:
    data1.write(data)

playsound(loc)