import pyaudio, sys, socket
import sys
import threading
import uuid
import base64
from CallCenter import CallCenter
import SocketManager
from SpeechToText import SpeechToText
from pydub import AudioSegment
import wave
import speech_recognition as sr
from pydub.playback import play
import numpy as np

cc = CallCenter()
lines = ["line_01", "line_02", "line_03"]
cc.lineQueueInitiator(lines)

port = 4948
ip = "localhost"

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 32000

p = pyaudio.PyAudio()
stream = p.open(format = FORMAT, channels = CHANNELS, rate = RATE, input = True,output = True, frames_per_buffer = CHUNK)

#Create a socket connection for connecting to the server:
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))

# def thread_function():
#     try:
#         cc.getFromQueue(lines[1])
#     except:
#         print("")
    

# x = threading.Thread(target=thread_function)
# x.start()

recognizer = sr.Recognizer()
counter = 0
try:
    while True:
        counter += 1
        data = client_socket.recv(CHUNK)
        print(f"\n\n{counter}\n")
        print(data[:30])
        # audio = recognizer.record(data)
        # sound = AudioSegment(
        #     data=data,
        #     sample_width=2,
        #     frame_rate=16000,
        #     channels=1
        # )
        # play(sound)
        # fgghghjjhg = sound.export(format="wav")
        # audio = recognizer.record(sound)
        # text111 = recognizer.recognize_google(audio)
        # # stt = SpeechToText()
        # # text = stt.speechToText(audio)
        # _tempdData1 = base64.b64encode(data)
        # cc.pushToQueue(lines[2], _tempdData1)
        stream.write(data)
except KeyboardInterrupt:
    pass

print('Shutting down')
client_socket.close()
stream.close()
p.terminate()