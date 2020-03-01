import base64

with open("z_chunk0.mp3", mode='rb') as file: # b is important -> binary
    fileContent = file.read()

data = b'foo'.decode('UTF-8')

ff= fileContent

fff1 = base64.b64encode(ff)
fff2 = base64.b64decode(fff1)

print("End Python file")