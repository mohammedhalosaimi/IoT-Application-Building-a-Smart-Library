#!/usr/bin/env python3
# Reference: https://realpython.com/python-sockets/
# Documentation: https://docs.python.org/3/library/socket.html

import socket
from library_menu import library_menu
import logging

logging.basicConfig(filename="library.log", level = logging.ERROR)
class mp_socket:

    def connection(self, test = None):
        testPassed = False
        HOST = ""    # Empty string means to listen on all IP's on the machine, also works with IPv6.
                    # Note "0.0.0.0" also works but only with IPv4.
        PORT = 65000 # Port to listen on (non-privileged ports are > 1023).
        ADDRESS = (HOST, PORT)
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(ADDRESS)
                s.listen()
                
                print("Listening on {}...".format(ADDRESS))
                if(test == "test_setupServer"):
                    return True
                conn, addr = s.accept()
                with conn:
                    print("Connected to {}".format(addr))
                    if(test == "test_ConnectToServer"):
                        testPassed = True
                    else:
                        while True:
                            data = conn.recv(4096)
                            if(not data):
                                break

                            print("Received {} bytes of data decoded to: '{}'".format(
                                len(data), data.decode()))
                            message = data.decode() #Received message from RP
                            if(message == "loggedin"): #If user has successfully loggedin
                                # Call library menu
                                message  = library_menu.runMenu()
                                if(message == "loggedout"):
                                    conn.sendall(message.encode())
                                else:
                                    conn.sendall(message.encode()) 

                    print("Disconnecting from client.")
                print("Closing listening socket.")
            print("Done.")
        except  Exception as e:
            logging.error("MP Socket error: {}".format(str(e)))
        return testPassed

if __name__ == "__main__":
    mp_socket().connection()
