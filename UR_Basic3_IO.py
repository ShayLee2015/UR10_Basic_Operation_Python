# UR robot is the server, host computer is the client

import socket
import time

### change me - same as your UR controller IP
HOST_ROBOT = "192.168.1.120"
PORT_ROBOT = 30002
###

print("Starting Program")

# Communication:method 2 - socket.socket
robot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
robot_socket.connect((HOST_ROBOT, PORT_ROBOT))

# send the IO commands
print("sending the IO commands...")
tcp_command = "set_digital_out(3,False)\n"
robot_socket.send(str.encode(tcp_command))
time.sleep(1)


tcp_command = "set_digital_out(3,True)\n"
robot_socket.send(str.encode(tcp_command))
time.sleep(1)

# finish
robot_socket.close()
