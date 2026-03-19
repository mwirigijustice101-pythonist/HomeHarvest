from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#Auntheticate with Google Drive
google_auth = GoogleAuth()
google_auth.LocalWebserverAuth()
drive_app = GoogleDrive(google_auth)

#List of files to upload
upload_list = ["test.png","test.jpg"]

#Folder ID from Google Drive (replace "FOLDER_ID_FROM_GOOGLE_DRIVE"with your folder's ID)
folder_id = "FOLDER_ID_FROM_GOOGLE_DRIVE"

#Upload each file in the list
for file_to_upload_list:
    file = drive_app.CreateFile({"parents":[{"id": folder_id}]})
    file.setContentFile(file_to_upload)
    file.Upload()
    print(f"Uploaded{file_to_upload} successfully!")