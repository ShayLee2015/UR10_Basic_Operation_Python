# UR 10 - Basic Operation 2- movej _ two points
# Python 3.5
# UR robot is the server, host computer is the client


import socket
import time

### change me - same as your UR controller IP
HOST_ROBOT = "192.168.1.120"
PORT_ROBOT = 30002
###


print("Starting Program.")

# Communication:method 2 - socket.socket
robot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
robot.connect((HOST_ROBOT, PORT_ROBOT))
time.sleep(2) # wait for 2 second
print("Connected.")

# way-point
qd1 = 'movej([0.0,-1.57,0.0,-1.57,0.0,0.0],a=2.0,v= 0.5,r=0.01)\n' #joint commands, unit: radian
robot_socket.send(str.encode(qd1))
time.sleep(5) # wait for 5 second


qd2 = 'movej([ 0.22,-1.35079633  ,0.22,-1.35079633 ,-0.22,0],a=1.0,v= 0.05,r=0.01)\n' #joint commands, unit: radian
robot_socket.send(str.encode(qd2))
time.sleep(5) # wait for 5 second

# close the communication
robot.close()
print("Close the program.")
