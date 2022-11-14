from Google import Create_Service
import base64
from email.mime. multipart import MIMEMultipart
from email.mime. text import MIMEText
CLIENT_SECRET_FILE = 'secret.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']
service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
emailMsg = 'Hello\nTest 101 - Sending Email\n\nThank you\n'
mimeMessage = MIMEMultipart()
mimeMessage['to'] ='pics.general.backup.maha@gmail.com '
mimeMessage['subject'] = "Hi Maha's RasberryPi Here"

mimeMessage. attach (MIMEText(emailMsg, 'plain' ) )
raw_string = base64.urlsafe_b64decode(mimeMessage.as_bytes().decode())
message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
print(message)


# pip install -upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib