import socket
import sys
print('Starting echo-client')

HOST = '127.0.0.1'
PORT = 65432


def printMenu():
    print("What do you want to do?")
    print("1. Retrieve the text in the server")
    print("2. Update the text in the server")
    print("3. Close")

userInput = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((HOST, PORT))

    while userInput != 3:
        printMenu()
        userInput = int(input())

        if not 0 < userInput < 4:
            print("Please enter a valid integer choice!\n")
            continue

        if userInput == 3:
            print("Socket closed from client")
            sys.exit()
        s.send(str(userInput).encode('utf-8'))
        if userInput == 2:
            newWord = input("What text do you want to update with?\n")
            s.sendall(newWord.encode("utf-8"))
        data = s.recv(1024)

        print('Received', repr(data.decode("utf-8")), "\n")

