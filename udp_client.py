import socket

Host = 'localhost'
Port = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

massage = 'Hello from cli udp'

s.sendto(massage.encode(),(Host, Port))

data , address = s.recvfrom(1024)
print(data.decode())