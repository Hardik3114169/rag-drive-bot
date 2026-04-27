from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload
import io

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def get_drive_service():
    creds = service_account.Credentials.from_service_account_file(
        'credentials.json', scopes=SCOPES)
    return build('drive', 'v3', credentials=creds)


# ✅ FETCH FILE LIST
def fetch_files():
    service = get_drive_service()

    results = service.files().list(
        pageSize=10,
        fields="files(id, name)"
    ).execute()

    files = results.get('files', [])
    return files


# ✅ DOWNLOAD FILE CONTENT
def download_file(file_id):
    service = get_drive_service()

    request = service.files().get_media(fileId=file_id)
    file = io.BytesIO()

    downloader = MediaIoBaseDownload(file, request)

    done = False
    while not done:
        status, done = downloader.next_chunk()

    file.seek(0)
    return file.read()