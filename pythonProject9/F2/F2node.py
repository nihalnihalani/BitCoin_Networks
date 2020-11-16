from _curses import nl
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
turn=1
count=0

print ('The server is ready to receive')

def WriteTemp(Trasaction,count):

    Tempfile = open("/Users/nihalnihalani/PycharmProjects/pythonProject9/F2/TempF2.txt", "+a")
    Tempfile.writelines(Trasaction)
    Tempfile.write("\n")
    Tempfile.close()
    count+=1
    print(count)

    return count

def checkCounter(count,turn):
    if turn%2!=0:
        if count%4==0:
            print("Mine the Block")
            Mining()

            return
    else:
        return

def Mining():
    hashing=[]
    Tempfile = open("/Users/nihalnihalani/PycharmProjects/pythonProject9/F2/TempF2.txt", "r")
    for x in Tempfile:
        hashing.append(x.strip())
    print(hashing)





while 1:
    Trasaction,clientAddress = serverSocket.recvfrom(2048)
    Trasaction = Trasaction.decode()
    print(Trasaction)
    count=WriteTemp(Trasaction,count)
    checkCounter(count,turn)



