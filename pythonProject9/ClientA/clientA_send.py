from socket import *
import socket
serverName = 'localhost'
serverPortF1 = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverPortF2=2000

serverName = 'localhost'
uncomfirmtx = open("/Users/nihalnihalani/Desktop/Github/BitCoin_Networks/pythonProject9/ClientA/Unconfirmed_A.txt", "w")
transaction_fee=2


def NewTransaction(O=None):
    while True:
        Payer = input("Select the Payer: \n1.A0000001\n2.A0000002\n")
        if Payer == '1':
            Payer_account = "A0000001"
            with open("/Users/nihalnihalani/Desktop/Github/BitCoin_Networks/pythonProject9/ClientA/Balance_A.txt") as f:  # reads middle part for uncomfirmed balance for first account
                data=(f.readlines()[0])
            print(type(data))
            f.close()
            uncon = data[9:17]
        elif Payer == '2':
            Payer_account = "A0000002"
            with open("/Users/nihalnihalani/Desktop/Github/BitCoin_Networks/pythonProject9/ClientA/Balance_A.txt") as f:  # reads middle part for uncomfirmed balance for second account
                data = f.readlines()[1]
            print(data)
            f.close()
            uncon = data[9:17]
        print(Payer_account)
        Payee = input("Select the Payee \n1.B0000001\n2.B0000002\n")
        if Payee == '1':
            Payee_account = "B0000001"
        elif Payee == '2':
            Payee_account = "B0000002"
        print(Payee_account)
        Amount = int(input("Enter the amount in decimal:"))
        un_dec = int(uncon, 16)  # converts uncomfirmed balnce to decimal
        AmountTX = Amount + transaction_fee
        if (AmountTX > un_dec):
            print("Invalid transaction")
        else:
            AmountH = str.format('{:08X}', int(hex(Amount), 16))
            print(AmountH)
            un_dec = un_dec - Amount
            un_hex = str.format('{:08X}', int(hex(un_dec), 16))
            print(un_hex)
            Trasaction = Payer_account + Payee_account + AmountH
            print(Trasaction)
            clientSocket.sendto(Trasaction.encode(), (serverName, serverPortF1))
            clientSocket.sendto(Trasaction.encode(), (serverName, serverPortF2))
            uncomfirmtx = open("/Users/nihalnihalani/Desktop/Github/BitCoin_Networks/pythonProject9/ClientA/Unconfirmed_A.txt", "a+")
            uncomfirmtx.writelines(Trasaction)
            uncomfirmtx.write("\n")


def currentBalance():
    f = open("/Users/nihalnihalani/Desktop/Github/BitCoin_Networks/pythonProject9/ClientA/Balance_A.txt","r")
    for x in f:
        print(x)
    return


def UnconfirmedTX():
    uncomfirmtx = open("/Users/nihalnihalani/Desktop/Github/BitCoin_Networks/pythonProject9/ClientA/Unconfirmed_A.txt", "r")
    for x in uncomfirmtx:
        print(x)
    return


def LastXconfirmedTransactions(X):
    with open("/Users/nihalnihalani/Desktop/Github/BitCoin_Networks/pythonProject9/ClientA/Confirmed_A.txt") as file:
        for line in (file.readlines()[-X:]):
            print(line, end='')
    return

def Blockchain():
    f1 = open("/Users/nihalnihalani/Desktop/Github/BitCoin_Networks/pythonProject9/F1/BlockchainF1.txt", "r")
    Lines = f1.readlines()
    i=0
    for line in Lines:
        print("Block{}".format(i))
        print("Nounce:{}""\nLast Block hash:{}""\nMerkle Root:{}""\nTX1:{}""\nTX2:{}""\nTX3:{}""\nTX4{}".format(line[0:8],line[8:72],line[72:136],line[136:160],line[160:184],line[184:208],line[208:232]))
        i=+1
    return

def BlockCreated(done):
    if done=="1":
        f = open('/Users/nihalnihalani/Desktop/Github/BitCoin_Networks/pythonProject9/ClientA/Unconfirmed_A.txt')
        f1 = open('/Users/nihalnihalani/Desktop/Github/BitCoin_Networks/pythonProject9/ClientA/Confirmed_A.txt', 'a')
        for x in f.readlines():
            f1.write(x)
        f.close()
        f1.close()
    return


while True:
    print("==================")
    print("1.Enter a new transaction")
    print("2.The current balance for each account.")
    print("3.Print the unconfirmed transactions.")
    print("4.Print the last X number of confirmed transactions")
    print("5.Print the blockchain ")
    print("===================")
    choice = input("Please Select the Option:")
    if choice == '1':
        NewTransaction()
    elif choice == '2':
        currentBalance()
    elif choice == '3':
        UnconfirmedTX()
    elif choice == '4':
        done, serverAddress = clientSocket.recvfrom(2048)
        done = done.decode()
        BlockCreated(done)
        X = int(input("Enter the number of last confirmed Transactions you want to print\t"))
        LastXconfirmedTransactions(X)
    elif choice == '5':
        Blockchain()
    else:
        break

