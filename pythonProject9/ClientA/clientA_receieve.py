from socket import *

while 1:
    serverName = 'localhost'
    clientPortA = 20000
    clientSocketA = socket(AF_INET, SOCK_DGRAM)
    clientSocketA.bind(('', clientPortA))
    clientSocket.connect((serverName, serverPortA))
    C = open('/Users/nihalnihalani/Desktop/Github/BitCoin_Networks/pythonProject9/ClientA/Confirmed_A.txt', 'a')
    modifiedMessage, serverAddress = clientSocketA.recvfrom(2048)
    confirmed_tx = modifiedMessage.decode()
    #print(confirmed_tx)
    C.write(confirmed_tx + '\n')
    #clientSocketA.close()

