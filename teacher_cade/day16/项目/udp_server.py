#!/usr/bin/python3

from socket import *

#  64K
udp_socket = socket(AF_INET, SOCK_DGRAM)
addr_port = ('', 2000)
udp_socket.bind(addr_port)
recv_data = udp_socket.recvfrom(1024)
print(type(recv_data[1]))
print("ip %s gets %s" % (str(recv_data[1]), recv_data[0]))
udp_socket.sendto(b"I receive your message", recv_data[1])
udp_socket.close()
