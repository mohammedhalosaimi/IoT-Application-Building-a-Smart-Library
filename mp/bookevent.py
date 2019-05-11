# pip3 install google-api-python-client google-auth-httplib2 google-auth-oauthlib oauth2client httplib2
# python3 add_event.py --noauth_local_webserver

# Reference: https://developers.google.com/calendar/quickstart/python
# Documentation: https://developers.google.com/calendar/overview

# Be sure to enable the Google Calendar API on your Google account by following the reference link above and
# download the credentials.json file and place it in the same directory as this file.

from __future__ import print_function
from datetime import datetime
from datetime import timedelta
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import time
from pytz import timezone

class bookevent:
    @staticmethod
    def insert(username, isbn,title,author):
        # If modifying these scopes, delete the file token.json.
        SCOPES = "https://www.googleapis.com/auth/calendar"
        store = file.Storage("token.json")
        creds = store.get()
        if(not creds or creds.invalid):
            flow = client.flow_from_clientsecrets("credentials.json", SCOPES)
            creds = tools.run_flow(flow, store)
        service = build("calendar", "v3", http=creds.authorize(Http()))
        date = datetime.now(timezone('Australia/Melbourne'))
        curr_time=date.time()
        next_week = (date + timedelta(days = 7)).strftime("%Y-%m-%d")
        time_start = "{}T{}".format(next_week,curr_time)
        time_end = "{}T{}".format(next_week,curr_time)
        event = {
            "summary": "Return Book",
            "location": "IoT Smart Library",
            "description": "Username: {} has borrowed book details ISBN: {}  Title: {}  Author: {} ".format(username, isbn,title,author),
            "start": {
                "dateTime": time_start,
                "timeZone": "Australia/Melbourne",
            },
            "end": {
                "dateTime": time_end,
                "timeZone": "Australia/Melbourne",
            },
            "id": isbn,
            "reminders": {
                "useDefault": False,
                "overrides": [
                    { "method": "email", "minutes": 5 },
                    { "method": "popup", "minutes": 10 },
                ],
            }
        }

        try:
            event = service.events().insert(calendarId = "primary",  body = event).execute()
            print("Event created: {}".format(event.get("htmlLink")))
        except:
            event = service.events().update(calendarId='primary', eventId=isbn, body=event).execute()

    @staticmethod
    def removeEvent(isbn):
        SCOPES = "https://www.googleapis.com/auth/calendar"
        store = file.Storage("token.json")
        creds = store.get()
        if(not creds or creds.invalid):
            flow = client.flow_from_clientsecrets("credentials.json", SCOPES)
            creds = tools.run_flow(flow, store)
        service = build("calendar", "v3", http=creds.authorize(Http()))
        # this function does not delete the event, rather it hides it and changes the status to 'cancell'
        service.events().delete(calendarId = "primary", eventId = isbn).execute()

# 12345 --> resolve adding and deleting this isbn
bookevent.insert('Mohammed', '23456', 'Why Me', 'Mohammed Alotaibi')
# removeEvent('23456')