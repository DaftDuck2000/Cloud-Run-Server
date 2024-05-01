import socket 
import requests

def get_public_ip():
    try:
        response = requests.get('https://httpbin.org/ip')
        if response.status_code == 200:
            data = response.json()
            return data['origin']
        else:
            return "Failed to retrieve public IP"
    except requests.RequestException as e:
        return "Error: {}".format(e)
    
if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     
    public_ip = get_public_ip()
    
    server_socket.bind((public_ip, 8000))
    
    server_socket.listen(5)
    
    while True:
        client_socket, client_address = server_socket.accept()
        print("Connection from:", client_address)