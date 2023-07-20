#include <stdio.h>
#include <stdlib.h>
#include <arpa/inet.h>


int main() {
    int client_socket;
    struct sockaddr_in server_address;
    int random_number;

    // Create socket
    client_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (client_socket == -1) {
        perror("Error creating socket");
        exit(EXIT_FAILURE);
    }

    server_address.sin_family = AF_INET;
    server_address.sin_addr.s_addr = inet_addr("10.0.2.15"); // Server IP address 
    server_address.sin_port = htons(8080); // Server port 

    // Connect to the server
    if (connect(client_socket, (struct sockaddr*)&server_address, sizeof(server_address)) == -1) {
        perror("Error connecting to the server");
        exit(EXIT_FAILURE);
    }

    // Receive the random number from the server
    if (recv(client_socket, &random_number, sizeof(random_number), 0) == -1) {
        perror("Error receiving data");
    } else {
        printf("Received random number from server: %d\n", random_number);
    }

    // Close the socket
    close(client_socket);

    return 0;
}
