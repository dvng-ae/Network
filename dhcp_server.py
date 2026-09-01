import socket
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("localhost",45000))

print("DHCP server started.......")
print("waiting for client request........")

ip_pool = ['192.168.1.10','192.168.1.11','192.168.1.12']
 
while True:
 	message,address = server.recvfrom(1024)
 	message = message.decode()
 	
 	print("Client: ",message)
 	
 	if message == "DHCPDISCOVER":
 		ip = ip_pool[0]
 	
 		server.sendto(("DHCPOFFER"+ip).encode(),address)
 	
 		print("Offered IP :",ip)

 	elif message.startswith("DHCPREQUEST"):
 		ip = message.split()[0]		
 	
 		server.sendto(("DHCPACK"+ip).encode(),address)
 	
 		print("Assigned IP : ", ip)
 		break
server.close()	
