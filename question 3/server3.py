import socket

def convert_to_atmosphere(pressure_bar):
    atmosphere = pressure_bar * 0.986923
    return atmosphere

def handle_client(client_socket):
    try:
        data = client_socket.recv(1024)
        pressure_bar = float(data.decode())
        atmosphere = convert_to_atmosphere(pressure_bar)
        client_socket.send(str(atmosphere).encode())

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()


def main():
    server_address = "10.0.2.15"
    server_port = 8080

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_address, server_port))
    server_socket.listen(1)

    print("Server is listening for incoming connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        handle_client(client_socket)
if __name__ == "__main__" :
main()
