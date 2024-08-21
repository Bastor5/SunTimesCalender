import datetime
import requests
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from dateutil.relativedelta import relativedelta

# Constants
LOCATION = "Tel Aviv, Israel"
API_URL = "https://api.sunrise-sunset.org/json"
SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_sunrise_sunset_times(lat, lng, date):
    params = {
        'lat': lat,  # Latitude for the location
        'lng': lng,  # Longitude for the location
        'formatted': 0,
        'date': date
    }
    response = requests.get(API_URL, params=params)
    data = response.json()
    return data['results']['sunrise'], data['results']['sunset']

def authenticate_google_calendar():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def create_calendar_event(service, start_time_utc, end_time_utc, summary, attendee_email):
    event = {
        'summary': summary,
        'start': {'dateTime': start_time_utc, 'timeZone': 'Asia/Jerusalem'},
        'end': {'dateTime': end_time_utc, 'timeZone': 'Asia/Jerusalem'},
        'attendees': [{'email': attendee_email}],
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f'Event created: {event.get("htmlLink")}')

def main():
    # Set up authentication
    creds = authenticate_google_calendar()
    service = build('calendar', 'v3', credentials=creds)

    # Set the location coordinates for Tel Aviv, Israel
    lat = 32.0853
    lng = 34.7818

    # Get today's date and the end date (one month from today)
    start_date = datetime.date.today()
    end_date = start_date + relativedelta(months=1)

    # Iterate over each day in the next month
    current_date = start_date
    while current_date <= end_date:
        # Get the date in the required format
        date_str = current_date.strftime('%Y-%m-%d')

        # Get sunrise and sunset times for the current date
        sunrise, sunset = get_sunrise_sunset_times(lat, lng, date_str)

        # Convert times to ISO 8601 format
        sunrise_time = datetime.datetime.fromisoformat(sunrise).isoformat()
        sunset_time = datetime.datetime.fromisoformat(sunset).isoformat()

        # Create events for sunrise and sunset
        create_calendar_event(service, sunrise_time, sunrise_time, f'Sunrise on {date_str}', 'ENTER YOUR EMAIL HERE')
        create_calendar_event(service, sunset_time, sunset_time, f'Sunset on {date_str}', 'ENTER YOUR EMAIL HERE')

        # Move to the next day
        current_date += datetime.timedelta(days=1)

if __name__ == '__main__':
    main()
