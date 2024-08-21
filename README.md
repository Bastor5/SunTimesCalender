THIS ISN'T THE FULL VERSION OF THE PROGRAM AND IT WILL NOT WORK IF YOU DON'T COMPLETE THE STEPS LISTED BELOW:

1. Go to Google Cloud Console
Visit the Google Cloud Console.
If prompted, sign in with your Google account.

2. Create or Select a Project
At the top, click on the project drop-down (it might show "Select a project" if you don’t have any projects).
Select an existing project or click "New Project" to create a new one. Give your project a name and click "Create."

3. Navigate to the Credentials Page
In the left-hand sidebar, click on “API & Services” to expand it.
Then, click on “Credentials.”

4. Create OAuth 2.0 Client ID
On the Credentials page, click the “+ CREATE CREDENTIALS” button at the top of the page.
From the dropdown, select “OAuth 2.0 Client ID.”

5. Configure OAuth Consent Screen
If this is your first time creating OAuth credentials, you’ll be prompted to set up the OAuth consent screen.
Choose "External" if you are sharing this with other users outside your Google Workspace (like inviting your Email account).
Fill in the required fields such as App Name, User Support Email, and Developer Contact Information.
After completing the form, click “Save and Continue” until you reach the “Summary” page, then click “Back to Dashboard.”

6. Create the OAuth Client ID
After setting up the consent screen, you'll be prompted to choose the application type. Select “Desktop app”.
Enter a name for your OAuth client (e.g., "SunriseSunsetApp").
Click “Create.”

7. Download the credentials.json File
After creating the OAuth 2.0 Client ID, a screen will appear with your client ID and client secret.
Click “Download JSON” to download the credentials.json file.
Save this file in the same directory where you’ll have your Python script.

8. Finish Up
You now have the credentials.json file, which your Python program will use to authenticate with the Google Calendar API.

Why This Is Important:
The credentials.json file contains the necessary information for your application to access the Google Calendar API on behalf of your Google account. When your program runs, it will use this file to request permission to manage your Google Calendar, and you'll authorize it through a web browser.
