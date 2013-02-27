import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.bind(('localhost',18001))  
sock.listen(100)  

while True:
    connection,address = sock.accept()
    try:
        connection.settimeout(100)
        buf = connection.recv(1024)
        if buf == '1':
            connection.send('welcome to server!')
        else:
                connection.send('please !')
    except socket.timeout:
        print 'time out'
    connection.close()
                

