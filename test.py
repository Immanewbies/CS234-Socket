
import csv

from numpy import row_stack
scnum = 0
i = 0
"""
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
"""
#read user name and password from csv
file = open("user_pass.csv")
csvreader = csv.reader(file)
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
file.close()

print(rows)

for x in rows:
    print(x[0])
    s = x[0]
    
    
    