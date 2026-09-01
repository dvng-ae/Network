import socket
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address = ("localhost",45000)

client.sendto("DHCPDISCOVER".encode(),server_address)
print("Client :DHCPDISCOVER sent")

message,address = client.recvfrom(1024)
message = message.decode()

print("Server:",message)

if message.startswith("DHCPOFFER"):
	ip = message.split()[0]
	
	client.sendto(("DHCPREQUEST"+ip).encode(),server_address)
	
	print("Client: DHCPREQUEST sent")
	
	message,address = client.recvfrom(1024)
	print("Server: ",message)
client.close()	
