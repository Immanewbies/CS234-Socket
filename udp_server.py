import socket

Host = 'localhost'
Port = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((Host, Port))

massage_sv = 'Hello from Sv udp'
while True:
    try:
        data, address = s.recvfrom(1024)
        if data:
            print(data.decode())
            s.sendto(massage_sv.encode(), address)
    finally:
        s.close()
    break