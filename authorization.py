from oauth2client import client
import sys
import credentials


def main():
 flow = client.OAuth2WebServerFlow(
     client_id=credentials.client_id,  # client id
     client_secret=credentials.client_secret,  # client secret
     scope=credentials.scopes,
     user_agent='Python Developement Client Library',
     redirect_uri=credentials.redirect_uri,
     access_type='offline')

 authorize_url = flow.step1_get_authorize_url()

 print ('Log into the Google Account you use to access your Analytics account'
        'and go to the following URL: \n{}\n\nAfter approving the token enter '
        'the verification code (if specified).'.format(authorize_url))

 code = input('Code: ').strip()

 try:
   credential = flow.step2_exchange(code)

   printtext=('OAuth 2.0 authorization successful!\n\n'
              'Your access token is:\n {}\n\nYour refresh token is:\n {}'
              .format(credential.access_token, credential.refresh_token))

   print(printtext)

 except :
   sys.exit(1)

if __name__ == '__main__':
 main()