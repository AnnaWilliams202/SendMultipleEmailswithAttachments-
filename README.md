# SendMultipleEmailswithAttachments-
The code will read the list of email addresses from emails.txt and send an email with body message to each address. The script will print a confirmation message for each email sent successfully.
Install Required Libraries:
Ensure you have the necessary libraries installed by running the following command in your terminal:

pip install yagmail python-dotenv
Create the .env File:

In the same directory as your script, create a .env file and add your Gmail password as follows:
GMAIL_PASSWORD=your_gmail_password

Prepare the Email List:
Create a file named emails.txt containing the list of email addresses to which you want to send the email. Each email address should be on a new line.

Library Imports:
The script imports yagmail for sending emails and dotenv for loading environment variables from the .envfile.

Load Environment Variables:
It loads the Gmail password from the .env file using dotenv.load_dotenv().

SMTP Server Initialization:
An instance of yagmail.SMTP is created using the sender's email address and password, allowing the script to send emails.

Email Content:
The subject and body of the email are defined in variables.

Reading Email Addresses:
The script opens emails.txt, reads the email addresses, and strips any whitespace characters.

Sending Emails:
The script iterates through the list of recipient emails, sending the defined email to each one. After sending each email, it prints a confirmation message.

genarate gmail app password


