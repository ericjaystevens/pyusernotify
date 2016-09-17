# pyusernotify
Allows sys admins to email users of events using prepared messages, this allows you to keep the email format and code required to send an email seperate from the logic of your automated trigger event, script, or application. 

Instructions for use
====================

prepare template
----------------

create an email template text file to create the body of your text. Use markdown syntex. The first  two lines will not be part of your email. name the file example.pun

### Example Template

~~~~
from: admin@example.com
subject: Password Will Expire soon!

sir or madam,

Your Password will expire soon? Visit [This Link](www.passwordreset.example.com) to reset your password before you are locked out!

Sincerly,

Your IT Team

![Logo](/path/to/img.jpg )
~~~~~

You can then send the email message, by calling the webservice from your script or application. 

This example is in powershell but the webservice can be consumed in any language. 
~~~{powershell}
New-WebServiceProxy -Uri http://yourIP:5000/send/example/user@example.com -ErrorAction:SilentlyContinue
~~~

The user will then be sent an html based email, based on the content of your templeate.

<p>sir or madam,</p>

<p>Your Password will expire soon? Visit <a href="www.passwordreset.example.com">This Link</a> to reset your password before you are locked out!</p>

<p>Sincerly,</p>

<p>Your IT Team</p>

<p><img src="/path/to/img.jpg " alt="Logo" /></p>








