import socket
import pyaudio
import select

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 40960

audio = pyaudio.PyAudio()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 4943))

def callback(in_data, frame_count, time_info, status):
    s.send(in_data)
    return (None, pyaudio.paContinue)

stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK, stream_callback=callback)

# read_list = [sm]
read_list = [serversocket]
print ("recording...")

# while (l):
#     sm.send(l)
#     print("Sent " + repr(l))
#     l = f.read(64000)

#     print("Done sending")
# sm.close()

try:
    while True:
        data = client_socket.recv(1024)
	    stream.write(data,CHUNK)
except KeyboardInterrupt:
    pass


print ("finished recording")

sm.close()
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()