import socket
import csv
import base64

# Read port and secret_key from .config file 
server_config  = open("server.config", "r")
read_config = server_config.read()
contents = read_config.splitlines()
content_linezero = contents[0].split("=")
content_lineone = contents[1].split("=")
# Assign values
Host = 'localhost'
Port = int(content_linezero[1])
Secretkey = content_lineone[1]
r = 0 
rnd = 1
rnd1= 1
rnd2 = 1
scnum = 0
# Read values from .csv file
file = open("user_pass.csv")
csvreader = csv.reader(file)
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
file.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((Host, Port))
s.listen()
while True:
    data, address = s.accept()
    try:
        
        while True:
            message = data.recv(10240)
            if message:
                clientmessage = message.decode()
                cl_message_sp = clientmessage.split(":")
                user1 = rows[0][0]+':'+rows[0][1]
                user2 = rows[1][0]+':'+rows[1][1]
                user1_k = rows[0][0]+'.'+rows[0][1]+'.'+Secretkey
                user2_k = rows[1][0]+'.'+rows[1][1]+'.'+Secretkey
                if r == 0:
                    if  clientmessage == user1:
                        format_mes = cl_message_sp[0]+'.'+cl_message_sp[1]+'.'+Secretkey
                        message_bytes = format_mes.encode()
                        base64_bytes = base64.b64encode(message_bytes)
                        base64_string = base64_bytes.decode()
                        message_sv = 'token:'+base64_string
                        r = r+1
                        data.sendto(message_sv.encode(), address)
                    elif  clientmessage == user2:
                        format_mes = cl_message_sp[0]+'.'+cl_message_sp[1]+'.'+Secretkey
                        message_bytes = format_mes.encode()
                        base64_bytes = base64.b64encode(message_bytes)
                        base64_string = base64_bytes.decode()
                        message_sv = 'token:'+base64_string
                        r = r+1
                        data.sendto(message_sv.encode(), address)
                        break
                    else:
                        if rnd == 3:
                            message_sv = 'Connection refused!! you’ve exceeded maximum number of attempts'
                            data.sendto(message_sv.encode(), address)
                            break
                        else:
                            message_sv = 'Invalid username or password'+str(rnd)+'/3 times'
                            data.sendto(message_sv.encode(), address)
                            rnd = rnd+1
                elif r == 1:
                    token_mes = cl_message_sp[0]
                    base64_tkbytes = token_mes.encode()
                    message_tkbytes = base64.b64decode(base64_tkbytes)
                    message_tkstring = message_tkbytes.decode()
                    if message_tkstring == user1_k:
                        message_sv = 'Authenticated : true'
                        data.sendto(message_sv.encode(), address)
                        r = r+1    
                    elif message_tkstring == user2_k:
                        message_sv = 'Authenticated : true'
                        data.sendto(message_sv.encode(), address)
                        r = r+1
                    else:
                        if rnd1 == 3:
                            message_sv = 'Connection refused!! you’ve provided wrong tokens 3 times in a row'
                            data.sendto(message_sv.encode(), address)
                            break   
                        else:
                            message_sv = 'Authenticated :false'
                            data.sendto(message_sv.encode(), address)
                            rnd1 = rnd1+1
                elif r == 2:
                    token_mes = cl_message_sp[0]
                    base64_tkbytes = token_mes.encode()
                    message_tkbytes = base64.b64decode(base64_tkbytes)
                    message_tkstring = message_tkbytes.decode()
                    if message_tkstring == user1_k:
                        if cl_message_sp[1] == 'request secret number':
                            e = int(cl_message_sp[2])
                            n = int(cl_message_sp[3])
                            sp_user = int(message_tkstring.split('.',2)[0])
                            sp_username = [int(a) for a in str(sp_user)]
                            scnum = sum(sp_username)
                            encryptsc = pow(scnum,e,n)
                            message_sv = 'Encrypted Secret Number:'+ str(encryptsc)
                            data.sendto(message_sv.encode(), address)
                        elif cl_message_sp[1] == 'check secret number':
                            scnum_recv = int(cl_message_sp[2])

                            if scnum == scnum_recv:
                                message_sv = 'Secret Number Verification: true'
                                data.sendto(message_sv.encode(), address)
                            else:
                                message_sv = 'Secret Number Verification: false'
                                data.sendto(message_sv.encode(), address)
                        elif cl_message_sp[1] == 'quit':
                            message_sv = 'Session is closed.'
                            data.sendto(message_sv.encode(), address)
                            break
                        else:
                            message_sv = 'Connection refused !! Invalid Action.'
                            data.sendto(message_sv.encode(), address)
                            break
                    elif message_tkstring == user2_k:
                        if cl_message_sp[1] == 'request secret number':
                            e = int(cl_message_sp[2])
                            n = int(cl_message_sp[3])
                            sp_user = int(message_tkstring.split('.',2)[0])
                            sp_username = [int(a) for a in str(sp_user)]
                            scnum = sum(sp_username)
                            encryptsc = pow(scnum,e,n)
                            message_sv = 'Encrypted Secret Number:'+ str(encryptsc)
                            data.sendto(message_sv.encode(), address)
                        elif cl_message_sp[1] == 'check secret number':
                            scnum_recv = int(cl_message_sp[2])
                            if encryptsc == scnum_recv:
                                message_sv = 'Secret Number Verification: true'
                                data.sendto(message_sv.encode(), address)
                            else:
                                message_sv = 'Secret Number Verification: false'
                                data.sendto(message_sv.encode(), address)
                        elif cl_message_sp[1] == 'quit':
                            message_sv = 'Session is closed.'
                            data.sendto(message_sv.encode(), address)
                            break
                        else:
                            message_sv = 'Connection refused !! Invalid Action.'
                            data.sendto(message_sv.encode(), address)
                            break
                    else:
                        if rnd2 == 3:
                            message_sv = 'Connection refused!! you’ve provided wrong tokens 3 times in a row'
                            data.sendto(message_sv.encode(), address)
                            break   
                        else:
                            message_sv = 'Authenticated :false'
                            data.sendto(message_sv.encode(), address)
                            rnd2 = rnd2+1   
    finally:
        s.close()
    break