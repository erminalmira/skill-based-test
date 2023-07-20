import socket

def get_user_input():
    try:
        pressure_bar = float(input("Enter pressure value in bar: "))
        return pressure_bar
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None

def main():
    server_address = "10.0.2.15"
    server_port = 8080

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_address, server_port))
    pressure_bar = None
    while pressure_bar is None:
        pressure_bar = get_user_input()

   
    client_socket.send(str(pressure_bar).encode())
    atmosphere = float(client_socket.recv(1024).decode())
    print(f"Received atmosphere-standard value from server: {atmosphere:.2f} atm")
    client_socket.close()

if __name__ == "__main__":
    main()
