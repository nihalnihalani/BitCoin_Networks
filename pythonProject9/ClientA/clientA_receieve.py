from socket import *
import os
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ('The Client A is ready to receive')
ClientA = ["A0000001", "A0000002"]

while 1:
    transaction, clientAddress = serverSocket.recvfrom(2048)
    transaction = transaction.decode()
    if len(transaction)==24:
        payer,payee,amount = transaction[0:8],transaction[8:16],transaction[16:24]
        uncomfirmtx = open("/Users/nihalnihalani/Desktop/Github/BitCoin_Networks/pythonProject9/ClientA/Unconfirmed_A.txt", "a+")
        uncomfirmtx.writelines(transaction)
        uncomfirmtx.write("\n")




#
#
#
# while 1:
#
#     if len(message.decode()) == 24:
#         # check whether my client is a payer of payee
#         transaction = message.decode()
#         payer = transaction[0:8]
#         payee = transaction[8:16]
#         amount = transaction[16:24]
#
#         with open("Unconfirmed_T.txt", 'r+') as Unconfirmed_File:
#             unconfirmed_transactions = Unconfirmed_File.read().splitlines()
#
#             # Check to see if my account is a Payer
#             if payer in myAccounts:
#                 # Check to see if transaction is my Unconfirmed_T
#                 if transaction in unconfirmed_transactions:
#
#                     unconfirmed_transactions.remove(transaction)
#
#                     Unconfirmed_File.seek(0)
#                     Unconfirmed_File.truncate()
#
#                     # Adds new line to each transaction and writes it to Unconfirmed_T
#                     for transactionLine in unconfirmed_transactions:
#                         transactionLine = transactionLine + '\n'
#                         Unconfirmed_File.write(transactionLine)
#                     # Appends confirmed transaction to Confirmed_T
#                     with open("Confirmed_T.txt", 'a') as Confirmed_File:
#                         Confirmed_File.write(transaction + '\n')
#
#                     # Reduces Confirmed Balance of payer by Tx amount + Tx fee
#                     with open("balances.txt", 'r+') as Balance_File:
#                         confirmedBalances = Balance_File.read().splitlines()
#                         Balance_File.seek(0)
#                         Balance_File.truncate()
#                         for balanceLine in confirmedBalances:
#                             balanceLine = balanceLine.split(":")
#                             if balanceLine[0] == payer:
#                                 balanceLine[2] = "{:08x}".format(int(balanceLine[2], 16) - int(amount, 16) - 2)
#
#                             Balance_File.write(":".join(balanceLine) + '\n')
#
#             elif payee in myAccounts:
#                 # Appends confirmed transaction to Confirmed_T
#                 with open("Confirmed_T.txt", 'a') as Confirmed_File:
#                     Confirmed_File.write(transaction + '\n')
#                 with open("balances.txt", 'r+') as Balance_File:
#                     confirmedBalances = Balance_File.read().splitlines()
#                     Balance_File.seek(0)
#                     Balance_File.truncate()
#                     for balanceLine in confirmedBalances:
#                         balanceLine = balanceLine.split(":")
#                         if balanceLine[0] == payee:
#                             balanceLine[1] = "{:08x}".format(int(balanceLine[1], 16) + int(amount, 16))
#                             balanceLine[2] = "{:08x}".format(int(balanceLine[2], 16) + int(amount, 16))
#
#                         Balance_File.write(":".join(balanceLine) + '\n')
#
#     else:
#         exec(message.decode())
#
