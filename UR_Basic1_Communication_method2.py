# UR 10 - Basic Operation 1- communication (second method)
# Python 3.5
# UR robot is the server, host computer is the client


import socket
import time

### change me - same as your UR controller IP
HOST_ROBOT = "192.168.1.120"
PORT_ROBOT = 30002
###

print("Starting Program")

# Communication:method 2 - socket.socket
robot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
robot.connect((HOST_ROBOT, PORT_ROBOT))

time.sleep(2) # wait for 2 second
print("Connected.")

robot.close()
