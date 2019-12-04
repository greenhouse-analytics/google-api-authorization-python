# Set up a Google API connection in Python #

This repository will help you set up a connection to a Google API in Python using Google OAuth. 
The benefit of using OAuth over a serveris account is that it uses your Google user accounts to connect to the API. 
You can use the credentials you create here in other projects that use Google API's.

To do this successfully, follow the following three steps:

## 1 Set up a Google project ##

For step one: you'll need to set up a Google Project here: https://console.developers.google.com. After you've set up a project, create credentials for it. Use this configuration:

- Access type: OAuth Client ID
- Application type: Other

When you've configured your credentials, you'll see your client id and client secret. You will need these in step 2.

## 2 Get your access token and refresh token ##

After creating a project, you'll have to generate an access token and refresh token. 
You can do so by creating `credentials.py` based of `credentials-example.py`. 
Fill out the client id and client secret that you've generated in step 1. 
Make sure to fill out [the scopes for the APIs](https://developers.google.com/identity/protocols/googlescopes) you want to use. After that, run `authorize.py`. This will print a URL in the console and asks you to fill out a code. Click the URL to authorize your Google Account. After that, you'll see a screen with the 'code value'. Copy-paste this in the console of your Python editor. After this, the console will print your access token and refresh token.

*If you have to redo the API connection, make sure to remove your app's access from your account ([use this link](https://security.google.com/settings/security/permissions)). It's required because Google only gives you a refresh token on your first successful access request.*


## 3. Connect to the API ##

The final step: test your connection. 
You can modify `connect.py` to connect to your API of choice. 
The console will print an object if the connection is successful. 
If so, you're ready to use the credentials in another project. 
To do so, move the credentials and connect files over to your new project.

```
<googleapiclient.discovery.Resource object at 0x00000215242759E8>
```
