# Reference: https://realpython.com/python-sockets/
# Documentation: https://docs.python.org/3/library/socket.html

# import socket
# import logging
# import json

# logging.basicConfig(filename="library.log", level = logging.ERROR)
class rp_socket:
        """
            **Recieption Socket**

            RP Socket is to connect Recieption Pi to the Master Pi. By running the Recieption station and successful login, this socket
            will communicate with the master PI and transfers the success login message and user name to the mastert pi.
            This socket then listens to the master pi for logout message. After logout request the method passes this message to the user class to 
            prepare the station for the next login.

            - Example::

                Received username:'Mark' from user class. 


            - Expected Success Response::

                Connected to 127.0.0.0:65000

        """
#     # Call connection after successful login
#     def connection(self, user="test"):    
#         try:
#             jsonData = self.readConfig()
#             HOST = jsonData["hostname"]
#             PORT = jsonData["port"]  
#             ADDRESS = (HOST, PORT)
#             with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#                 s.connect(ADDRESS)
#                 print("Connected to {}...".format(ADDRESS))

#                 while True:               
#                     s.sendall(user.encode())
#                     # listen to message from server:
#                     data = s.recv(4096)
#                     message = data.decode()
#                     print("Message from MP: " + message)
#                     if(message == "logout"):
#                         return message
#         except  Exception as e:
#             logging.error("RP Socket error: {}".format(str(e)))
#             print(str(e))



#     # Read config.json
#     def readConfig(self):
#         with open('config.json') as jsonFile:  
#             data = json.load(jsonFile)
#         return data


# if __name__ == "__main__":
#     rp_socket().connection()