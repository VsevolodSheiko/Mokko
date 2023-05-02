


from google.oauth2 import service_account
from googleapiclient.discovery import build
from coffeehouse.models.visitor import Visitor
from datetime import date

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1Bpd2tLthwjwvD3EWZjHull7T6DjbnMPvFMeaYkRpx2I'
SAMPLE_RANGE_NAME = 'Лист1!A2:E'

def get_service():
    credentials = service_account.Credentials.from_service_account_file("service_account.json")
    service = build('sheets', 'v4', credentials=credentials)
    
    return service


def read():
    service = get_service()
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    print(values)


def write():
    visitors = Visitor.objects.filter(date_joined=date.today())
    values = [[visitor.id, visitor.first_name, visitor.last_name, visitor.email, visitor.date_joined] for visitor in visitors]
    visitors.delete()
    service = get_service()
    sheet = service.spreadsheets()
    sheet.values().update(
        spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range=SAMPLE_RANGE_NAME,
        valueInputOption="USER_ENTERED",
        body={"values": values}
    ).execute()
