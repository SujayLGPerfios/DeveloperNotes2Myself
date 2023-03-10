# Description: Send an HTTP Request Using TCP Socket in Python

import socket

# Create a TCP connection to the HTTP Server on port 80.
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket.connect(('www.posttestserver.com', 80))

# Create an HTTP GET Request message strictly adhering to the HTTP RFC 2616.
httpRequestMessage = b"GET / HTTP/1.1\r\nHost:www.posttestserver.com\r\n\r\n"
tcpSocket.send(httpRequestMessage)

while 1:
    data = tcpSocket.recv(1024)
    if not len(data):
        break
    print(data)

# Close the TCP Connection
tcpSocket.close()

# The output of the above code snippet will be an HTTP Response message similar to the one below,
#
# HTTP/1.1 200 OK
# Date: Tue, 16 Dec 2014 07:36:01 GMT
# Server: Apache
# Access-Control-Allow-Origin: *
# Vary: Accept-Encoding
# Content-Length: 140
# Connection: close
# Content-Type: text/html
#
# Successfully dumped 0 post variables.
# View it at http://www.posttestserver.com/data/2014/12/15/23.36.01167058517
# Post body was 0 chars long.
