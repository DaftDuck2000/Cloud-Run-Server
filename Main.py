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
    
print(get_public_ip())