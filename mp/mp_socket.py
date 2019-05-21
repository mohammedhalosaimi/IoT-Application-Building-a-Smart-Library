#!/usr/bin/env python3
# Reference: https://realpython.com/python-sockets/
# Documentation: https://docs.python.org/3/library/socket.html

import socket
from library_menu import library_menu
import logging

logging.basicConfig(filename="library.log", level = logging.ERROR)
class mp_socket:
    def connection(self, test = None):
        """
        Server connetion is to start a TCP socket on the Master Pi (server) so that all reception PIs can connect to the server.
        On setting up the connection, server listens to the connection requests and the coming messages.
        This message will be the logged in user name which will be used for book borrowing purpose.
        When the user selects logout from the library menu, the server will send "logout" message to RP
        and RP is required to logout the user. The server stands by until another user logs in

        Parameters:

        Returns:

        """
        testPassed = False
        HOST = ""    # Empty string means to listen on all IP's on the machine, also works with IPv6.
                    # Note "0.0.0.0" also works but only with IPv4.
        PORT = 65000 # Port to listen on (non-privileged ports are > 1023).
        ADDRESS = (HOST, PORT)
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.bind(ADDRESS)
                s.listen()
                print("Listening on {}...".format(ADDRESS))
                # Test server connection:
                if(test == "test_setupServer"):
                    return True
                while True:
                    print("The Smart Library is Ready be Accessed! Waiting for a User to Login . . .")
                    conn, addr = s.accept()
                    with conn:
                        print("Connected to {}".format(addr))
                        # test client connection
                        if(test == "test_ConnectToServer"):
                            testPassed = True
                        else:
                            data = conn.recv(4096)
                            if(data):
                                #Received message from RP   
                                user = data.decode() 
                                # print("Message from rp: " + user)
                                # Call library menu to search books/borrow books/return books
                                logout_req  = library_menu().runMenu(user)
                                if(logout_req == "logout"):
                                    conn.sendall(logout_req.encode())

                        print("Disconnecting from client.")
                    print("Closing listening socket.")
            print("Done.")
        except  Exception as e:
            logging.error("MP Socket error: {}".format(str(e)))
            print(str(e))
        #finally:
            # Clean up the connection
         #   conn.close()
        return testPassed

if __name__ == "__main__":
    mp_socket().connection()
