from CallCenter import CallCenter
import threading
import uuid
import base64

from scipy.io import wavfile
fs, data = wavfile.read('1.wav')

cc = CallCenter()
lines = ["line_01", "line_02", "line_03"]

f = open("1.wav", "rb")

def thread_function():
    try:
        cc.getFromQueue(lines[2])
    except:
        print("")
        
thread_function()