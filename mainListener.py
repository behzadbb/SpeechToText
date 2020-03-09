import SocketManager
from CallCenter import CallCenter
import uuid
import base64
import pyaudio
#import socket
import sys
import threading

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 40960

sm = SocketManager.SocketManager()
cc = CallCenter()
lines = ["line_01", "line_02", "line_03"]

cc.lineQueueInitiator(lines)

sm.setPort("localhost", 6465, CHUNK)
sm.serverStart()

def thread_function():
    textxx = cc.getFromQueue(lines[0])
    if textxx:
        print("\nNewText:\n", textxx)

x = threading.Thread(target=thread_function)
x.start()

while True:
    conn, addr = sm.accept()     # Establish connection with client.
    print('Got connection from', addr)
    
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)
    counter=1
    try:
        while True:
            data = conn.recv(sm.packetSize)
            stream.write(data)
            print(counter ,"  data size: ",data.__len__())
            counter +=1
            _tempdData1 = base64.b64encode(data)
            cc.pushToQueue(lines[0], _tempdData1)
    except KeyboardInterrupt:
        pass

    # itteration = 0
    # _guid = str(uuid.uuid4())
    # buffer = b""
    # buffer1 = b""
    # with open('received_file.wav', 'wb') as f:
    
    # while True:
        
    #     # print('data=%s', (data))
    #     if not data:
    #         break
    #     buffer += data
    #     print(data.__len__())
    #     if counter % 4 == 0 :
    #         buffer1 += buffer
    #         _tempdData1 = base64.b64encode(buffer1)
    #         cc.pushToQueue(lines[0], _tempdData1)
    #         buffer1 = b""
        
    #     counter += 1

    # _tempdData = buffer
    # _tempdData = base64.b64encode(_tempdData)
    # cc.pushToQueue(lines[0], _tempdData)
    # textxx = cc.getFromQueue(lines[0])
    
