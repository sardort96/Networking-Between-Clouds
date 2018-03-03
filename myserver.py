import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('',6457))

s.listen(5)

c = s.accept()

# open the file and write to it what is received 
with open('File1.txt', 'w') as file_write:
	file_content = c.recv(1024)
	while len(file_content)>0:
		file_write.write(file_content)
		file_content = c.recv(1024)
		# set a delimiter to know when to transfer to another file
		if 'Sardor' in file_content:
			break


with open('File2.txt', 'w') as file_write2:
	file_content2 = c.recv(1024)
	while len(file_content2)>0:
		file_write2.write(file_content2)
		file_content2 = c.recv(1024)
		if 'Sardor' in file_content2:
			break

with open('File3.txt', 'w') as file_write3:
	file_content3 = c.recv(1024)
	while len(file_content3)>0:
		file_write3.write(file_content3)
		file_content3 = c.recv(1024)
		if 'Sardor' in file_content3:
			break


c.close()

