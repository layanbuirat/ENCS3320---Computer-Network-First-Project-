import socket

def main():
    # Define the port number based on student ID
    port = 1439
    server_address = ('localhost', port)

    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    try:
        # Send data
        message = input("Enter a string to send to the server: ")
        client_socket.sendall(message.encode())
        # Receive the response
        modified_data = client_socket.recv(1024).decode()
        print(f"Received modified data from server: {modified_data}")
    finally:
        # Close the socket
        client_socket.close()

if __name__ == "__main__":
    main()
