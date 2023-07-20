import socket

def send_receive_data(server_address, server_port, data):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_address, server_port))
        client_socket.sendall(data.encode())
        server_response = client_socket.recv(1024).decode()
        client_socket.close()

        return server_response

    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    server_address = "izani.synology.me"
    server_port = 8443

    student_id = "2021486388"

    response = send_receive_data(server_address, server_port, student_id)

    if response is not None:
        print(f"Server Response: {response}")

    else:
        print("Connection failed or no response received.")
if __name__=="__main__":
        main()
