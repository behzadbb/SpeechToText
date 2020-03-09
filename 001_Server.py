import pyaudio, sys, socket

port = 5000
chunk = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(format = FORMAT, channels = CHANNELS, rate = RATE, input = True, output = True, frames_per_buffer = chunk)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create the socket
server_socket.bind(('', port)) # listen on port 5000
server_socket.listen(5) # queue max 5 connections
client_socket, address = server_socket.accept()

print ("Your IP address is: ", socket.gethostbyname(socket.gethostname()))
print ("Server Waiting for client on port ", port)

while True:

    # test string
    #data = bytearray('DEADBEEF'.decode('hex'))
    #client_socket.sendall(data)
    
	try:
		client_socket.sendall(stream.read(chunk))
	except IOError,e:
		if e[1] == pyaudio.paInputOverflowed: 
			print e 
			x = '\x00'*16*256*2 #value*format*chunk*nb_channels 

stream.stop_stream()
stream.close()
socket.close()
p.terminate()