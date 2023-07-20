import socket

def main():
   
    server_address = "10.0.2.15"
    server_port = 8888

 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((server_address, server_port))
        print("Connected to the QOTD server.")
        quote = client_socket.recv(1024).decode()
        print("Received Quote of the Day:")
        print(quote)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
