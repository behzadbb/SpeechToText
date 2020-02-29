import socket

class SocketManager:
    host = "localhost"
    port = 60000
    packetSize = 64000
    socket = socket.socket()

    def setPort(self, host="localhost", port=60000, packetSize=64000):
        self.host = host
        self.port = port
        self.packetSize = packetSize

    def connect(self):
        self.socket.connect((self.host, self.port))

    def close(self):
        self.socket.close()

    def send(self, data):
        self.socket.send(data)

    def recive(self):
        return self.socket.recv(self.packetSize)

    def serverStart(self, listenNumber=5):
        self.socket.bind((self.host, self.port))
        self.socket.listen(listenNumber)
    
    def accept(self):
        return self.socket.accept()