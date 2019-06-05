# Set up a Google API connection in Python #

This repository will help you set up a connection to a Google API in Python using Google OAuth. 
The benefit of using OAuth over a serveris account is that it uses your Google user accounts to connect to the API. 
You can use the credentials you create here in other projects that use Google API's.

To do this successfully, follow the following three steps:

## 1 Set up a Google project ##

For step one: you'll need to set up a Google Project. 
Read [Erwin Maas' amazing post about Google OAuth 2](https://www.themarketingtechnologist.co/google-oauth-2-enable-your-application-to-access-data-from-a-google-user/?utm_source=ghg_google_auth_repo&utm_medium=doc). 
Follow his 17 steps to create a project. After these 17 steps, you can continue to the second part of the setup in this repo. ***The interface referred to in the post has since been updated*** *, but the descriptions still work in the new interface.*

## 2 Get your access token and refresh token ##

After creating a project, you'll have to get your access token and refresh token. 
You can do so by creating `credentials.py` based of `credentials-example.py`. 
Fill out the credentials from your Google Project. 
Make sure to fill out [the scopes for the APIs](https://developers.google.com/identity/protocols/googlescopes) you want to use. 
After that, run `authorize.py`. 
This will print a URL in the console and asks you to fill out a code. 
You can get the code from the URL:

- Open the URL.
- Accept the conditions listed in the access request window (they should match the scopes you've configured)
- Copy the value of the `?code` URL parameter.
- Fill out the code in the console.

Et voila: the console just printed your access token and refresh token.

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
