---
{
	"_label": "Setting up Email"
}
---
Emails are the nervous system of business communication and Owrang has been designed to make good use of this. 

## Sending Emails

You can email any document from the system, by clicking on the “Email” button on the right sidebar. Before that you will need to set your outgoing email settings (SMTP server).

All emails sent from the system are added to the Communication table.

> **Info:** What is SMTP? There are two types of email services, sending and receiving emails. Sending is done via a protocol called SMTP (Simple Mail Transfer Protocol) and the server (computer) that sends your email to its destination is called SMTP Server.

> **Info:** Bulk Emails: Bulk Emails, especially those that are sent without consent (spam), are considered as bad behavior. While it may be okay to send emails to those who have “opted-in” to receive mails, it is very difficult for the internet community to know what is spam and what is allowed. To overcome this problem, most email servers share a black and white list of email senders. If your emails have been marked as spam, you will be blacklisted. So be careful. Many times, it may be a good idea to send email via whitelisted services also known as SMTP relay services which are paid services. These services will block you from sending spam while ensuring that most of your email does not go in the spam folder. There are many such services available like SendGrid and SMTP.com

To setup your outgoing mails, go to

> Setup > Outgoing Email Settings > Email Settings


![Email Settings](img/email-settings1.png)



Set your outgoing mail server settings here. These are the same settings you would use in your Outlook, Thunderbird, Apple Mail or other such email applications. If you are not sure, get in touch with your email service provider.

> **Tip:** If you are using EPRNext hosted service, keep the first section blank. Emails will still be sent from your email id, but via our SMTP relay service.

### Creating Support Tickets from Incoming Emails

A very useful email integration is to sync the incoming emails from support inbox into Support Ticket, so that you can track, assign and monitor support issues.

> **Case Study:** Here at Owrang, we have regularly tracked incoming support issues via email at “support@erpnext.com”. At the time of writing we had answered more than 3000 tickets via this system.

To setup your Support integration, go to:

> Setup > Support Email Settings > EMail Settings


![Email Settings](img/email-settings2.png)




To make Owrang pull emails from your mail box, enter the POP3 settings. (POP3 is a way of extracting emails from your mailbox. It should be fairly easy to find out what your POP3 settings are. If you have problems, contact your email service provider).
If you want to setup an auto reply, check on the “Send Autoreply” box and whenever someone sends an email, an autoreply will be sent.
Add a custom signature which you want to send with your replies. 

### Setting Auto-notification on Documents

Owrang allows you to automatically email documents on “Submission” to the contact mentioned in the document. To set this up, go to:

> Setup > Tools > Enable / Disable Notifications.


![Auto Notification](img/auto-notification.png)



Check on the transactions you want to send via email directly on Submission and add a custom message if you want on these documents.
￼
### Email Digests

Email Digests allow you to get regular updates about your sales, expenses and other critical numbers directly in your Inbox. 

Set your frequency, check all the items you want to receive in your weekly update and select the user ids whom you want to send the Digest to.

Email Digests are a great way for top managers to keep track of the big numbers like “Sales Booked” or “Amount Collected” or “Invoices Raised” etc.

To setup Email Digests, go to: 

> Setup > Email Digest > New Email Digest 


![Email Digest](img/email-digest.png)
