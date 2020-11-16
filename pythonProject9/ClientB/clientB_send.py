from socket import *
import socket

serverName = 'localhost'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverName = 'localhost'
uncomfirmtx = open("/Users/nihalnihalani/PycharmProjects/pythonProject9/ClientB/Unconfirmed_B.txt", "w")




def NewTransaction():
    while True:
        Payer = input("Select the Payer: \n1.A0000001\n2.A0000002\n")
        if Payer == '1':
            Payer_account = "B0000001"
        elif Payer == '2':
            Payer_account = "B0000002"
        print(Payer_account)
        Payee = input("Select the Payee \n1.B0000001\n2.B0000002\n")
        if Payee == '1':
            Payee_account = "A0000001"
        elif Payee == '2':
            Payee_account = "A0000002"
        print(Payee_account)
        Amount = int(input("Enter the amount in decimal:"))
        AmountH = str.format('{:08X}', int(hex(Amount), 16))
        print(AmountH)
        Trasaction=Payer_account+Payee_account+AmountH
        print(Trasaction)
        clientSocket.sendto(Trasaction.encode(), (serverName, serverPort))
        uncomfirmtx = open("/Users/nihalnihalani/PycharmProjects/pythonProject9/ClientB/Unconfirmed_B.txt", "a+")
        uncomfirmtx.writelines(Trasaction)
        uncomfirmtx.write("\n")

        break


def currentBalance():
    return


def UnconfirmedTX():
    uncomfirmtx = open("/Users/nihalnihalani/PycharmProjects/pythonProject9/ClientB/Unconfirmed_B.txt", "w")
    for x in uncomfirmtx:
        print(x)
    return


def LastXconfirmedTransactions(X):
    with open("/ClientA/Confirmed_A.txt") as file:
        for line in (file.readlines()[-X:]):
            print(line, end='')
    return


def Blockchain():
    f1 = open("/Users/nihalnihalani/PycharmProjects/pythonProject9/F1/BlockchainF1.txt.txt", "r")
    print(f1.readline())
    f2 = open("/Users/nihalnihalani/PycharmProjects/pythonProject9/F2/BlockchainF2.txt.txt", "r")
    print(f2.readline())
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
        X = int(input("Enter the number of last confirmed Transactions you want to print\t"))
        LastXconfirmedTransactions(X)
    elif choice == '5':
        Blockchain()
    else:
        break
