# Reference: https://realpython.com/python-sockets/
# Documentation: https://docs.python.org/3/library/socket.html

import socket
import logging
import json

logging.basicConfig(filename="library.log", level = logging.ERROR)
class rp_socket:

    # Call connection after successful login
    def connection(self, user):    
        try:
            jsonData = self.readConfig()
            HOST = jsonData["hostname"]
            PORT = jsonData["port"]  
            ADDRESS = (HOST, PORT)
            print(HOST)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(ADDRESS)
                while True:               
                    s.sendall(user.encode())
                    # listen to message from server:
                    data = s.recv(4096)
                    message = data.decode()
                    if(message == "logout"):
                        print(message)
        except  Exception as e:
            logging.error("RP Socket error: {}".format(str(e)))
            print(str(e))



    # Read config.json
    def readConfig(self):
        with open('config.json') as jsonFile:  
            data = json.load(jsonFile)
        return data