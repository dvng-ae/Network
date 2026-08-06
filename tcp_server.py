import socket
server = socket.socket()
server.bind(("localhost",5000))
server.listen(1)
print("Waiting for client request")
client,addr = server.accept()
print("connected:",addr)
while True:
  message = client.recv(1024).decode()
  if message.lower() == 'exit':
    print("client Disconnected") 
    break
  print("Client : ",message)   
  
  reply = input("Server : ")
  client.send(reply.encode())
  
  if reply.lower() == 'exit':
    print("Server Disconnected") 
    break
client.close()
server.close()
print("Connection closed")

