import socket
import threading
import random

# List of quotes
quotes = [
"To be or not to be, that is the question.", 
"The only thing that stands between you and your dream is the will to try and the belief that it is actually possible.", 
"The journey of a thousand miles begins with a single step.", 
"The only way to do great work is to love what you do."
]

def get_random_quote():
    return random.choice(quotes)

def handle_client(client_socket):
    try:
        quote = get_random_quote()
        client_socket.send(quote.encode())

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()

def main():
    server_address = "10.0.2.15"
    server_port = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((server_address, server_port))
    server_socket.listen(5)

    print("Server is listening for incoming connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()
