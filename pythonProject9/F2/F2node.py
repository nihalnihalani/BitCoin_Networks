from _curses import nl
from socket import *
import hashlib


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
turn=1
count=0

print ('The server is ready to receive')

def WriteTemp(Trasaction,count):

    Tempfile = open("/Users/nihalnihalani/Desktop/Github/BitCoin_Networks/pythonProject9/F1/TempF1.txt", "+a")
    Tempfile.writelines(Trasaction)
    Tempfile.write("\n")
    Tempfile.close()
    count+=1
    print(count)

    return count

def checkCounter(count,turn):
    list2=[]
    if turn%2!=0:
        if count%4==0:

            print("Mine the Block")
            list2=Mining()

            return list2
    else:
        return

def Mining():
    hashing=[]
    Tempfile = open("/Users/nihalnihalani/Desktop/Github/BitCoin_Networks/pythonProject9/F1/TempF1.txt", "r")
    for x in Tempfile:
        hashing.append(x.strip())
    print(hashing)
    return hashing

def hash_input(input):
    m = hashlib.sha256()
    m.update("input".encode("utf-8"))
    return m.hexdigest()


class Merkleroot(object):
    def __init__(self):
        pass

    def findMerkleRoot(self, leafHash):
        hash = []
        hash2 = []
        if len(leafHash) % 2 != 0:  ##if not even, repeat the last element
            leafHash.extend(leafHash[-1:])

        for leaf in sorted(leafHash):  ##for each leaf
            hash.append(leaf)
            if len(hash) % 2 == 0:  ##only add  hash if there are two first hash
                hash2.append(hash_input(hash[0] + hash[1]))  ##run through hash func for both hashes
                hash == []  ##reset first hash to empty
        if len(hash2) == 1:  ##if  hash is only one, we are the root
            return hash2
        else:
            return self.findMerkleRoot(hash2)  ##if not, recurse with hash2


def get_merkle_root(transactions):
    leafHash = []
    ##compute a list of hashes from transactions
    for trans in transactions:
        leafHash.append(hash_input(trans))

    mr = Merkleroot()
    return mr.findMerkleRoot(leafHash)


while 1:
    Trasaction,clientAddress = serverSocket.recvfrom(2048)
    Trasaction = Trasaction.decode()
    print(Trasaction)
    count=WriteTemp(Trasaction,count)
    if count %4==0:
        list1=checkCounter(count,turn)
        print(get_merkle_root(list1))


