import socket

class socket_rp:

    @staticmethod
    def getSocket():
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        return UDPClientSocket

    @staticmethod
    def sendMessage(option,message):
        UDPClientSocket=socket_rp.getSocket()
        msgFromClient =option+","+message
        bytesToSend = str.encode(msgFromClient)
        serverAddressPort   = ("127.0.0.1", 20001)
        UDPClientSocket.sendto(bytesToSend,serverAddressPort)
    
    @staticmethod
    def getMessage():
        UDPClientSocket=socket_rp.getSocket()
        msgFromServer = UDPClientSocket.recvfrom(1024)
        msg = "{}".format(msgFromServer[0])
        return msg
