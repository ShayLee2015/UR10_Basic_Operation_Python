# UR 10 - Basic Operation 1- communication
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

# close the communication
robot.close()