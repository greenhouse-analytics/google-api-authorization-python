import oauth2client
import httplib2
import credentials
from googleapiclient.discovery import build


def main():
    client = oauth2client.client.GoogleCredentials(
        credentials.access_token,
        credentials.client_id,
        credentials.client_secret,
        credentials.refresh_token,
        3920,
        'https://accounts.google.com/o/oauth2/token',
        credentials.user_agent
    )

    http = httplib2.Http()
    http = client.authorize(http)
    service = build('sheets', 'v4', http=http)
    print(service)


if __name__ == '__main__':
 main()
