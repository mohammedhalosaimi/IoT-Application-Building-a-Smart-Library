#!/usr/bin/env python3
# Reference: https://realpython.com/python-sockets/
# Documentation: https://docs.python.org/3/library/socket.html

import socket
from library_menu import library_menu
import logging

logging.basicConfig(filename="library.log", level = logging.ERROR)
class mp_socket:
    # Server connetion is to run a server TCP socket to connect Reciption Pi to Master Pi.
    # On setting up the connection, server listens to the connection requests and the coming messages.
    # This message will be the logged in user name which will be used for book borrowing purpose.
    # When the user selects logout fromthe library menu, the server will send "logout" message to RP
    # and RP is required to logout the user  
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
                
                # Test server connection:
                if(test == "test_setupServer"):
                    return True
                conn = s.accept()
                with conn:
                    # test client connection
                    if(test == "test_ConnectToServer"):
                        testPassed = True
                    else:
                        while True:
                            data = conn.recv(4096)
                            if(not data):
                                break

                            user = data.decode() #Received message from RP

                            # Call library menu
                            logout_req  = library_menu.runMenu(user)
                            if(logout_req == "logout"):
                                conn.sendall(logout_req.encode())

                    print("Disconnecting from client.")
                print("Closing listening socket.")
            print("Done.")
        except  Exception as e:
            logging.error("MP Socket error: {}".format(str(e)))
        return testPassed

if __name__ == "__main__":
    mp_socket().connection()
