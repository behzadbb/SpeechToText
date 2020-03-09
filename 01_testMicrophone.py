import pyaudio
import socket
import sys

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 32768

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 4943))
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)
counter = 1
try:
    while True:
        data = s.recv(CHUNK)
        stream.write(data)
        print("\n" + str(counter) + "   Data Size: " + str(data.__len__()))
        counter += 1
except KeyboardInterrupt:
    pass

print('Shutting down')
s.close()
stream.close()
audio.terminate()