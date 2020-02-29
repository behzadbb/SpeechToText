import SocketManager

sm = SocketManager.SocketManager()

sm.setPort("localhost", 6465, 64000)

sm.connect()

f = open("1.wav", 'rb')
# l = f.read(1024)
l = f.read(64000)
while (l):
    sm.send(l)
    print("Sent " + repr(l))
    l = f.read(64000)

    print("Done sending")
sm.close()
