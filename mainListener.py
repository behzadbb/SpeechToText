import SocketManager
from CallCenter import CallCenter
import uuid
import base64

sm = SocketManager.SocketManager()
cc = CallCenter()
lines = ["line_01", "line_02", "line_03"]

cc.lineQueueInitiator(lines)

sm.setPort("localhost", 6465, 64000)
sm.serverStart()

while True:
    conn, addr = sm.accept()     # Establish connection with client.
    print('Got connection from', addr)

    itteration = 0
    _guid = str(uuid.uuid4())
    buffer = b""

    # with open('received_file.wav', 'wb') as f:
        
    while True:
        data = conn.recv(sm.packetSize)
        # print('data=%s', (data))
        if not data:
            break
        buffer += data
        print(data.__len__())
        # write data to a file
        # f.write(data)
        #audio = sr.AudioData(data,16000,2)
        #r = sr.Recognizer()
        #tempDat = r.recognize_google(audio,language="fa-IR")
        # print(tempDat)
        
    # _tempData = {
    #     "VOID": _guid,
    #     "Itteration": itteration,
    #     "VoiceData": buffer
    # }
    _tempdData = buffer
    _tempdData = base64.b64encode(_tempdData)
    cc.pushToQueue(lines[0], _tempdData)
    textxx = cc.getFromQueue(lines[0])
    
