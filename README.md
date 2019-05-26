# Smart Library - IoT application

In this project, we developed an application where we automated a Library ManagementSystem (LMS). This system will be used to borrow, return and maintain the backend information. 
The library user arrives at the reception. It is not manned by any person. TheRECEPTION PI (RP) provides two options available for logging into the system:- using console-based system which allows them to type in the user credentials or,- using a facial recognition systemThe user registration is required for the first-time user. Upon registration the details are stored in alocal database installed on RP. Upon logging in, a success message along with the username is sent from RP (Reception PI) to the MASTER PI (MP) via sockets. The user is now presented with another console-based application where the user can search for book catalogues based on ISBN/Author name/Book name (either by using console-based system or voice search feature) , option for borrowing a book/books, option for returning a book/books (either by typing the ISBN of a book or scanning the QR code), logout. Upon logging out a message is sent via sockets from MP to RP.
For library admin: This is a separate website application that runs on MP. It can only be accessedby admin personnel. Admin website makes use of an API to:
- Add books to catalogue
- Remove books
- Generate a data visualisation report for books borrowed (day and week wise)
The book database is stored on a cloud environment namely the Google’s GCP IoT platform(Google Cloud Platform).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites


```
In our implementation, we use two raspberry pis where one act like a reception and other one acts like a master. You can use you machine with two windows to get the application working. 
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Please find the installation.txt file where you will find all the necessary packages to install
```

## Running the tests

Explain how to run the automated tests for this system

```
You will need to run user.py file in one window and library_menu.py in another window
```


## Built With

* [Flask](http://flask.pocoo.org) - Python microframework
* [Google Cloud Platform](https://cloud.google.com/gcp/?utm_source=google&utm_medium=cpc&utm_campaign=japac-AU-all-en-dr-bkws-all-super-trial-e-dr-1003987&utm_content=text-ad-none-none-DEV_c-CRE_248263937479-ADGP_Hybrid%20%7C%20AW%20SEM%20%7C%20BKWS%20~%20T1%20%7C%20EXA%20%7C%20General%20%7C%201:1%20%7C%20AU%20%7C%20en%20%7C%20google%20cloud%20platform-KWID_43700023244271242-kwd-296644789888&userloc_9071338&utm_term=KW_google%20cloud%20platform&gclid=CjwKCAjw8qjnBRA-EiwAaNvhwDdJuPzXpsVzy8bM4AsttOQ86iB5Cz29fB-LU5AqkuNp86ayj2igQBoCFsUQAvD_BwE) - Google Cloud Platform
* [Google Calendar API](https://developers.google.com/calendar/) - Used to add, remove events on a user Google Calendar
* [Google Assistant SDK](https://developers.google.com/assistant/sdk/) - Used to translate voice to text
* [OpenCV](https://opencv.org) - Used to detect object via camera
* [Google Data Studio](https://datastudio.google.com/u/0/navigation/reporting) - Used to Generate a data visualisation report

## Authors

* **Mohammed Alotaibi** - [MohammedAlosaimi](https://github.com/mohammedhalosaimi)
* **Dawei Mao** - [maodawei](https://github.com/maodawei)
* **Brad Hill** - [Bradels](https://github.com/Bradels)
* **Farid Farzin** - [FaridFarzin](https://github.com/FaridFarzin)


## Acknowledgments

* Acknowledgments to COSC2674 - Programming Internet of Things code archives
* Inspiration

