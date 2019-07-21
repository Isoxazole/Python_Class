import socket

print('Starting echo-server')

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    client_sock, addr = s.accept()
    with client_sock:
        print('Connected by ', addr)
        text = "Hello, world"
        while True:
            data = client_sock.recv(1024)

            if not data:
                break
            choice = data.decode("utf-8")
            print(f"Received choice {choice}")
            if int(choice) == 1:
                client_sock.sendall(text.encode('utf-8'))
                print(f"Text returned: {text}\n")
            elif int(choice) == 2:
                newText = client_sock.recv(1024)
                text = newText.decode("utf-8")
                client_sock.sendall(b'Text changed!')
                print(f"Text updated to:f {text}\n")

        print("Socket closed from server")