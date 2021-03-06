import socket #that's the library

mysock = socket.socket(family=AF_INET, type=SOCK_STREAM) #create an object variable that will access a socket through the internet (arguments)
mysock.connect(('data.pr4e.org',80)) # now we connect using the host as the first argument and the port as the 2nd.
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.O\r\n\r\n'.encode() # create a variable to request information
    # don't know what HTTP/1.O\r\n\r\n' means
mysock.send(cmd) # it's connected. Now we need to send what we want through  AF_INET port 80 to the server
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print (data.decode())
mysock.close() #always important to close the connection
