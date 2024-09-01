from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to your service account key file
SERVICE_ACCOUNT_FILE = './secret_key.json'

# The scopes required for the application
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def authenticate_service_account():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build('drive', 'v3', credentials=creds)

def list_files_in_folder(drive_service, folder_id):
    query = f"'{folder_id}' in parents"
    results = drive_service.files().list(q=query).execute()
    items = results.get('files', [])
    
    if not items:
        print('No files found.')
    else:
        for item in items:
            file_name = item['name']
            file_id = item['id']
            file_link = f"https://drive.google.com/file/d/{file_id}/view"
            print(f"File Name: {file_name}, File Link: {file_link}")

if __name__ == '__main__':
    drive_service = authenticate_service_account()
    folder_id = '1Ma8-0mhOUQt-lhf5K6uYrx9TMt00Z1Xu'  # Replace with the actual shared folder ID
    list_files_in_folder(drive_service, folder_id)
