import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from time import sleep
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

for _ in range(212*5):
    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[1], None)
    sleep(0.2)