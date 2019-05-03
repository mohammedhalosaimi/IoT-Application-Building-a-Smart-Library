#!/usr/bin/env python3
# Reference: https://realpython.com/python-sockets/
# Documentation: https://docs.python.org/3/library/socket.html

import socket
import logging
import json
from user import user

logging.basicConfig(filename="library.log", level = logging.ERROR)
class rp_socket:
    def main(self):
        self.connection()
    # Call connection after successful login
    def connection(self):        
        try:
            jsonData = self.readConfig()
            HOST = jsonData["hostname"]
            PORT = jsonData["port"]  
            ADDRESS = (HOST, PORT)
            print(HOST)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                print("Connecting to {}...".format(ADDRESS))
                s.connect(ADDRESS)
                print("Connected.")
                # message = "loggedin" # to be removed
                while True:
                    # Call Login method, Method message should listen to MP for loggedout message
                    # message = login().login() # replace with login method
                    message = user.menu()

                    if(message == "loggedin"):                
                        s.sendall(message.encode())

                    # listen to message from server:
                    data = s.recv(4096)
                    print("Received {} bytes of data decoded to: '{}'".format(
                        len(data), data.decode()))
                    message = data.decode()
                    # if(message == "loggedout"):
                    #     loggedin = "loggedout"
                    #     break
        except  Exception as e:
            logging.error("RP Socket error: {}".format(str(e)))
            print(str(e))



    # Read config.json
    def readConfig(self):
        with open('config.json') as jsonFile:  
            data = json.load(jsonFile)
        return data

if __name__ == "__main__":
    rp_socket().main()
