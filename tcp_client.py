import socket
client = socket.socket()
client.connect(("localhost",5000))
print("Connected to server")

while True:
  message = input("Client :")
  client.send(message.encode())
  
  if message.lower() == 'exit':
    print("client Disconnected") 
    break  
  reply = client.recv(1024).decode()
  print("server : ",reply)

  if message.lower() == 'exit':
    print("server Disconnected") 
    break 

client.close()
print("Connection closed")
