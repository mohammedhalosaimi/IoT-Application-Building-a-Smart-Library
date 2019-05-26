# # pip3 install google-api-python-client google-auth-httplib2 google-auth-oauthlib oauth2client httplib2
# # python3 add_event.py --noauth_local_webserver

# # Reference: https://developers.google.com/calendar/quickstart/python
# # Documentation: https://developers.google.com/calendar/overview

# # Be sure to enable the Google Calendar API on your Google account by following the reference link above and
# # download the credentials.json file and place it in the same directory as this file.

# # Reference: COSC2674 - Programming Internet of Things - lab 8

# from __future__ import print_function
# from datetime import datetime
# from datetime import timedelta
# from googleapiclient.discovery import build
# from httplib2 import Http
# from oauth2client import file, client, tools
# import time
# from pytz import timezone

class bookevent:

    @staticmethod
    def insert(username, id,title,author):
    
        """
        Create an event on Google calendar if an event has not been created. OR delete an event if it exists

        Parameters:

        username, id 'Book ID', book title, author
        """

        # # If modifying these scopes, delete the file token.json.
        # SCOPES = "https://www.googleapis.com/auth/calendar"
        # store = file.Storage("token.json")
        # creds = store.get()
        # if(not creds or creds.invalid):
        #     flow = client.flow_from_clientsecrets("credentials.json", SCOPES)
        #     creds = tools.run_flow(flow, store)
        # service = build("calendar", "v3", http=creds.authorize(Http()))
        # date = datetime.now(timezone('Australia/Melbourne'))
        # curr_time=date.time()
        # next_week = (date + timedelta(days = 7)).strftime("%Y-%m-%d")
        # time_start = "{}T{}".format(next_week,curr_time)
        # time_end = "{}T{}".format(next_week,curr_time)
        # event = {
        #     "summary": "Return Book",
        #     "location": "IoT Smart Library",
        #     "description": "Username: {} has borrowed book details Book ID: {}  Title: {}  Author: {} ".format(username, id,title,author),
        #     "start": {
        #         "dateTime": time_start,
        #         "timeZone": "Australia/Melbourne",
        #     },
        #     "end": {
        #         "dateTime": time_end,
        #         "timeZone": "Australia/Melbourne",
        #     },
        #     "id": id,
        #     "reminders": {
        #         "useDefault": False,
        #         "overrides": [
        #             { "method": "email", "minutes": 5 },
        #             { "method": "popup", "minutes": 10 },
        #         ],
        #     }
        # }

        # # try to create an event if it doesn't exist with the id
        # try:
        #     event = service.events().insert(calendarId = "primary",  body = event).execute()
        #     print("Event created: {}".format(event.get("htmlLink")))
        # # update an event with the specified id if it already exists
        # except:
        #     event = service.events().update(calendarId='primary', eventId=id, body=event).execute()

    @staticmethod
    def removeEvent(id):

        """
        remove an event from Google Calendar with the given bookID

        Parameters: id 'Book ID'
        """

#         SCOPES = "https://www.googleapis.com/auth/calendar"
#         store = file.Storage("token.json")
#         creds = store.get()
#         if(not creds or creds.invalid):
#             flow = client.flow_from_clientsecrets("credentials.json", SCOPES)
#             creds = tools.run_flow(flow, store)
#         service = build("calendar", "v3", http=creds.authorize(Http()))
#         # this function does not delete the event, rather it hides it and changes the status to 'cancell'
#         service.events().delete(calendarId = "primary", eventId = id).execute()

# # bookevent.insert('LLLLL', '23456', 'Why Me', 'LLLLLL')
# # bookevent.removeEvent('23456')