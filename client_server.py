import socket
import ssl
import json
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8443)
    # Load client certificate and private key
    client_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    client_context.load_cert_chain(certfile=r'C:\Users\Suliat\PycharmProjects\transit\cert-1.pem',
                                   keyfile=r'C:\Users\Suliat\PycharmProjects\transit\key 1.pem')
    # Trust the self-signed certificate
    client_context.check_hostname = False
    client_context.verify_mode = ssl.CERT_NONE
    # Exclude SSLv2 and SSLv3 protocols
    client_context.options |= ssl.OP_NO_SSLv2
    client_context.options |= ssl.OP_NO_SSLv3
    # Set the minimum TLS version to TLS 1.2
    client_context.minimum_version = ssl.TLSVersion.TLSv1_2
    # Wrap the socket with SSL
    client_socket = client_context.wrap_socket(client_socket, server_hostname='localhost')
    # Connect to the server
    client_socket.connect(server_address)
    try:
        # eldercare health data
        health_data = {
            "patient_name": "Ayomikun",
            "age": 73,
            "blood_pressure": "120/80mmg",
            "heart_rate": 70,
            "temperature": 98.6
        }
        # Convert health data to JSON
        message = json.dumps(health_data)
        # Send health data to the server
        client_socket.sendall(message.encode('utf-8'))
        print("Sent health data to server:", message)
        # Receive the response from the server
        data = client_socket.recv(1024)
        print("Received response from server:", data.decode('utf-8'))
    finally:
        # Clean up the connection
        client_socket.close()
if __name__ == "__main__":
    start_client()