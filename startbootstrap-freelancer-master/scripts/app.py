from flask import Flask, render_template, request
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

app = Flask(__name__)

# Google Drive API credentials
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'My Drive/Uploads/New.json'  # Path to your service account JSON file

# Function to upload file to Google Drive
def upload_to_google_drive(file_path):
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)

    file_metadata = {
        'name': 'uploaded_file'
    }
    media = MediaFileUpload(file_path, resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    return file.get('id')

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file_path = 'uploads/' + file.filename
        file.save(file_path)
        uploaded_file_id = upload_to_google_drive(file_path)
        return 'File uploaded to Google Drive with ID: ' + uploaded_file_id

if __name__ == '__main__':
    app.run(debug=True)
