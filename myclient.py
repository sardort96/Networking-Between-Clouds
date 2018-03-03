import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('10.11.0.100', 6457))

# open the file and read the contents into a string to send it to the server

with open('aTaleOfTwoCities.txt', 'r') as file_read:
	chars = 100
	file_content = file_read.read(chars)
	while len(file_content)>0:
		s.send(file_content)
		file_content = file_read.read(chars)
	# send a delimiter for server to know when to write to a second file
	file_content = 'Sardor'
	s.send(file_content)



with open('mobydick.txt', 'r') as file_read2:
	chars = 100
	file_content2 = file_read2.read(chars)
	while len(file_content2)>0:
		s.send(file_content2)
		file_content2 = file_read2.read(chars)
	file_content2 = 'Sardor'
	s.send(file_content2)
	


with open('muchAdo.txt', 'r') as file_read3:
	chars = 100
	file_content3 = file_read3.read(chars)
	while len(file_content3)>0:
		s.send(file_content3)
		file_content3 = file_read3.read(chars)
	file_content3 = 'Sardor'
	s.send(file_content3)


s.close()
