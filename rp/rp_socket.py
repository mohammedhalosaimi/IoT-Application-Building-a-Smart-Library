# Reference: https://realpython.com/python-sockets/
# Documentation: https://docs.python.org/3/library/socket.html

import socket
import logging
import json

logging.basicConfig(filename="library.log", level = logging.ERROR)
class rp_socket:

    # Call connection after successful login
    def connection(self, user="test"):   
        """
        RP socket is called by user class if a user logs in successfully
        Parameters:

        Returns:
            logout message if the user logs out via MP
        """ 
        try:
            jsonData = self.readConfig()
            HOST = jsonData["hostname"]
            PORT = jsonData["port"]  
            ADDRESS = (HOST, PORT)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(ADDRESS)
                print("Connected to {}...".format(ADDRESS))
                print("Logging in as {}".format(user))
                print("Waiting for Master Pi...")
                while True:               
                    s.sendall(user.encode())
                    # listen to message from server:
                    data = s.recv(4096)
                    message = data.decode()
                    print("Message from MP: " + message)
                    if(message == "logout"):
                        return message
        except  Exception as e:
            logging.error("RP Socket error: {}".format(str(e)))
            print(str(e))



    # Read config.json
    def readConfig(self):
        """
        Fetch all the configuration paremeteres related to MP and make a connnection
        Parameters:

        Returns:
            Configruation data such as MP IP address
        """
        with open('config.json') as jsonFile:  
            data = json.load(jsonFile)
        return data


# if __name__ == "__main__":
#     rp_socket().connection()

