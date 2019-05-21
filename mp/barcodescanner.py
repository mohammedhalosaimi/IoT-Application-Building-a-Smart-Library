## This code is adapted from:
## https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-scanner-with-zbar/
## pip3 install pyzbar

# Reference: COSC2674 - Programming Internet of Things - lab 10

# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import datetime
import imutils
import time
import cv2
import re

class barcodescanner:
    @staticmethod
    def scanQR():

        """
        Scan a QR code and convert it to a string

        Returns: QR code string
        """

        # initialize the video stream and allow the camera sensor to warm up
        #https://www.qr-code-generator.com/
        # loop over the frames from the video stream
        while True:
            user_input=input("Please go to this website https://www.qr-code-generator.com/ to generate QR code with TEXT format.\nHit Enter to continue or q to quit")
            if(user_input=='q'):
                return "quitbyuser"
            print("Put QR Code in front of the camera")
            vs = VideoStream(src = 0).start()
            time.sleep(2.0)
            # grab the frame from the threaded video stream and resize it to
            # have a maximum width of 400 pixels
            frame = vs.read()
            frame = imutils.resize(frame, width = 400)
            # find the barcodes in the frame and decode each of the barcodes
            barcodes = pyzbar.decode(frame)
            # loop over the detected barcodes
            for barcode in barcodes:
                # the barcode data is a bytes object so we convert it to a string
                barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type
                # check if the user typed the ISBN
                regex= r'978[\d\-]+\d'
                pattern = re.match(regex, barcodeData)
                if bool(pattern)==True:
                    vs.stop()
                    return barcodeData   
                else:
                    print("QR does not follow the format.\nMake sure the format is 978-0-00-000000-0")
                vs.stop()
            # wait a little before scanning again
            time.sleep(1)
            vs.stop()
