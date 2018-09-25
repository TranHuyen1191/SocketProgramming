from socket import *

serverPort = 12000
try:
	serverSocket = socket(AF_INET, SOCK_DGRAM)
	serverSocket.bind(('', serverPort))
	print "The server is ready to receive!"
	while 1:
		message, clientAddress = serverSocket.recvfrom(2048)
		print 'Received message:' + str(message) + '	From' + str(clientAddress)
		modifiedMessage = message.upper()
		serverSocket.sendto(modifiedMessage, clientAddress)
except KeyboardInterrupt:
	print 'Catching Ctrl+C...!!!'
	serverSocket.close()

	