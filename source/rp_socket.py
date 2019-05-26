# # Reference: https://realpython.com/python-sockets/
# # Documentation: https://docs.python.org/3/library/socket.html

# import socket
# import logging
# import json

# logging.basicConfig(filename="library.log", level = logging.ERROR)
class rp_socket:

    # Call connection after successful login
    def connection(self, user="test"):   
        """
         RP Socket is called when a user is logged in. By that, the socket searches
         for the server IP address/port to connect with. On connecting to the MP
         User needs to refer to the MP station and follow the attempts.
         When MP requests for logout, this message is passed to user class to logout. 
        """ 
    #     try:
    #         jsonData = self.readConfig()
    #         HOST = jsonData["hostname"]
    #         PORT = jsonData["port"]  
    #         ADDRESS = (HOST, PORT)
    #         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #             s.connect(ADDRESS)
    #             print("Connected to {}...".format(ADDRESS))

    #             while True:               
    #                 s.sendall(user.encode())
    #                 # listen to message from server:
    #                 data = s.recv(4096)
    #                 message = data.decode()
    #                 print("Message from MP: " + message)
    #                 if(message == "logout"):
    #                     return message
    #     except  Exception as e:
    #         logging.error("RP Socket error: {}".format(str(e)))
    #         print(str(e))



    # # Read config.json
    # def readConfig(self):
    #     with open('config.json') as jsonFile:  
    #         data = json.load(jsonFile)
    #     return data