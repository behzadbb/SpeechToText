import SocketManager
from CallCenter import CallCenter
import uuid

sm = SocketManager.SocketManager()
cc = CallCenter()
lines = ["line_1", "line_2", "line_3"]

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
    cc.pushToQueue(lines[0], str(_tempData))
    textxx = cc.getFromQueue(lines[0])
