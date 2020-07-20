from socket import *

#  64K
udp_socket = socket(AF_INET, SOCK_DGRAM)
addr_port = ('192.168.1.111', 2000)
send_data = b"hello world"
print(type(send_data))
udp_socket.sendto(send_data, addr_port)
recv_data = udp_socket.recvfrom(1000)
print(recv_data[0])
udp_socket.close()
