import socket
import httplib
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.bind(('127.0.0.1',18001))  
sock.listen(100)  

while True:
    connection,address = sock.accept()
    try:
        connection.settimeout(100)
        buf = connection.recv(1024)
        #print buf
        for v in buf.split('\n'):
            print 'split' ,v
        
       # if buf == '1':
        #    connection.send('welcome to server!')
       # else:
         #       connection.send('please !')
        http = httplib.HTTPConnection('www.bilibili.tv')
        http.request("GET","/index.php")
        r1 = http.getresponse()
        connection.send(rl.read())
        
    except socket.timeout:
        print 'time out'
    connection.close()
                

