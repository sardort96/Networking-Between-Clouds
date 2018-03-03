# Networking-Between-Clouds
We provision a virtual machine running Linux on the Google Cloud Platform and write a server to transfer file data in Python. Then we write a client on another virtual machine and connect to the server. We create Google Compute Engine instances. An instance is a virtual machine that is hosted on Google's infrastructure. 
## Writing a Python Server 
Socket programming is a means of connecting two nodes on a network so that they can communicate with each other. One node listens on a particular port at an IP address, whereas other node connects to the other one. Server is considered a listener and client is the one that reaches out to the server. 

A server uses a 'bind()' method to bind the socket to a specific IP address and port in order to listen to incoming requests. It uses a 'listen()' method that puts the server to the listening mode. Server's 'accept()' method initiates a connection with a client. 

## Writing a Python Client
Client, instead of binding to a particular port and listening, connects to a server using its 'connect()' method to attach its socket directly using a remote IP address. 

