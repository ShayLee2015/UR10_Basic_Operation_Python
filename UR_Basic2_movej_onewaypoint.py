# UR 10 - Basic Operation 2- movej _ one point
# Python 3.5
# UR robot is the server, host computer is the client

import socket
import time

# set up your communication with UR
### change me - same as your UR controller IP
HOST_ROBOT = "192.168.1.120"
PORT_ROBOT = 30002
###

print("Starting Program.")

# Communication - create_connection
robot = socket.create_connection((HOST_ROBOT, PORT_ROBOT))
time.sleep(2) # wait for 2 second
print("Connected.")

# way-point
robot.send(b'movej([0.0,-1.57,0.0,-1.57,0.0,0.0],a=2.0,v= 0.5,r=0.01)\n') #joint commands, unit: radian
time.sleep(5) # wait for 2 second

# close the communication
robot.close()