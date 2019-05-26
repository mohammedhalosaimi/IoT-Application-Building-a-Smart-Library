.. Smart Library documentation master file, created by
   sphinx-quickstart on Sat May 18 09:47:21 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Smart Library's documentation!
=========================================
Configuration of Project Environment
*************************************

This system is provided to the local council library to automate the Library Management
System (LMS). This system will be used to borrow, return and maintain the backend information.
The application has two types of users: library user and library admin.
This system uses Google Calendar API to work with your Raspberry Pi using Google Cloud IoT Platform.

Application Components
======================
• Python documentation tools (Sphinx)
• Unit testing in Python
• Socket Programming
• An API using Python’s microframework Flask
• AI features (facial recognition, object detection and Voice detection)
• Cloud databases


Overview on How to Run this Application
=======================================
1. Download the app into two raspberry PIs, one is the master pi and the other is recieption pi
2. Install necessary packages mentioned on top of each class

Setup procedure
================
1. Master Pi
    On the MP Command line go to MP folder 
         - Type the command below on the command line environment. ::

            python3 mp_socket.py

2. Recieption Pi
    On the RP Command line go to RP folder 
         - Type the command below on the command line environment. ::

            python3 user.py

LMS features
============
    A. For library users: 
        The library user arrives at the reception. It is not manned by any person. The
        RECEPTION PI (RP) provides two options available for logging into the system:
            - using console-based system which allows them to type in the user credentials or,
            - using a facial recognition system
        The user registration is required for the first-time user. Upon registration the details are stored in a
        local database installed on RP.
        Upon logging in, a success message along with the username is sent from RP to the MASTER PI
        (MP) via sockets.
        The user is now presented with another console-based application:
            - search for book catalogues based on ISBN/Author name/Book name
            - option for borrowing a book/books
            - option for returning a book/books
            - logout
        Upon logging out a message is sent via sockets from MP to RP.

    B. For library admin: 
        This is a separate website application that runs on MP. It can only be accessed
        by admin personnel.
        Admin website makes use of an API to
            - Add books to catalogue
            - Remove books and
            - Generate a data visualisation report for books borrowed (day wise).
        The book database is stored on a cloud environment namely the Google’s GCP IoT platform
        (Google Cloud Platform).

Documentation for the Code
**************************
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   mp_socket
   mp_library_menu
   mp_database_utils
   mp_bookevent
   mp_barcodescanner
   mp_voice_recognition
   mp_controller
   mp_login_controller

   rp_user
   rp_socket
   rp_db
   rp_encode
   rp_capture
   rp_recognise



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
