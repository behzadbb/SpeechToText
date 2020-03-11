import SocketManager
from CallCenter import CallCenter
import uuid
import base64
import pyaudio
import socket
import sys
import threading
import select

# FORMAT = pyaudio.paInt16
# CHANNELS = 1
# RATE = 16000
# CHUNK = 40960

# sm = SocketManager.SocketManager()
# cc = CallCenter()
# lines = ["line_01", "line_02", "line_03"]

# cc.lineQueueInitiator(lines)

# sm.setPort("localhost", 6465, CHUNK)
# sm.serverStart()
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 32000

audio = pyaudio.PyAudio()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 4948))
serversocket.listen(5)

def callback(in_data, frame_count, time_info, status):
    for s in read_list[1:]:
        s.send(in_data)
    return (None, pyaudio.paContinue)

read_list = [serversocket]
print ("recording...")

# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK, stream_callback=callback)
# stream.start_stream()

try:
    while True:
        readable, writable, errored = select.select(read_list, [], [])
        for s in readable:
            if s is serversocket:
                (clientsocket, address) = serversocket.accept()
                read_list.append(clientsocket)
                print ("Connection from", address)
            else:
                data = s.recv(CHUNK)
                if not data:
                    read_list.remove(s)
except KeyboardInterrupt:
    pass

print ("finished recording")

serversocket.close()
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()