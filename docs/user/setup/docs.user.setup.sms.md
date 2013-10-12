---
{
	"_label": "SMS Setting"
}
---
To integrate SMS in Owrang, approach a SMS Gateway Provider who provides HTTP API. They will create an account for you and will provide an unique username and password.

To configure SMS Settings in Owrang, find out their HTTP API (a document which describes the method of accessing their SMS interface from 3rd party applications). In this document, you will get an URL which is used to send the SMS using HTTP request. Using this URL, you can configure SMS Settings in Owrang.

Example URL: <br>
<pre>http://instant.smses.com/web2sms.php?username=&lt;USERNAME>&password=&lt;PASSWORD>&to=&lt;MOBILENUMBER>&sender=&lt;SENDERID>&message=&lt;MESSAGE>
</pre>

![SMS Settings](img/sms-setting2.jpg)




> Note: the string up to the "?" is the SMS Gateway URL

Example:
<pre>http://instant.smses.com/web2sms.php?username=abcd&password=abcd&to=9900XXXXXX&sender
=DEMO&message=THIS+IS+A+TEST+SMS</pre>

The above URL will send SMS from account abcd to mobile number 9900XXXXXX with sender ID as DEMO with text message as "THIS IS A TEST SMS"

Note that some parameters in the URL are static.You will get static values from your SMS Provider like username, password etc. These static values should be entered in the Static Parameters table.

![SMS Setting](img/sms-settings1.png)

