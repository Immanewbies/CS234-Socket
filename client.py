import socket

HOST = 'localhost'
PORT = 8080
#socket()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #family = AF_INET , Stream socket = SOCK_STREAM

s.connect((HOST,PORT))
while True:
    Input = input("Say something:")
    s.sendto(str.encode(Input),(HOST,PORT))
    try:
        response = s.recv(10240)
        if response:
            print(response.decode())
        
    finally:
        print("Complete")

    
"""
import socket

Host = 'localhost'
Port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((Host, Port))
username = '5609610706'
password = '0706'

message = username+':'+password
print('Message in Client:',message)
s.sendto(message.encode() , (Host,Port))

message = "2222222222"+':'+password
print('Message in Client:',message)
s.sendto(message.encode() , (Host,Port))

message = "3333333333333"+':'+password
print('Message in Client:',message)
s.sendto(message.encode() , (Host,Port))

message = '5609610760'+':'+'0700'

s.sendto(message.encode(), (Host,Port))

data1 = s.recv(2048)
print(data1.decode())
"""


