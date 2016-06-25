# pyusernotify
Allows sys admins to email users of events using prepared messages, and allows users to opt out of nofication.

Instructions for use
====================

prepare template
----------------

create an email template text file to create the body of your text. Use markdown syntex. use $variableName to create replaceble items.  The first Line will be the subject of your email.

### Example Template

~~~~
Password Will Expire soon for $username

$firstname,

Your Password will expire soon? Visit [This Link](www.passwordreset.example.com) to reset your password before you are locked out!

Sincerly,

Your IT Team

![Logo](/path/to/img.jpg )
To opt out of this message click $optOutLink
~~~~~

Then initialize the new message

~~~~{.bash}
pyusernotify-newMessage -tempalte pathToTemplate.md -from fromAddress -name exampleMessageName 
~~~~~

You can then send the email message

~~~{.bash}
pyusernotify -message exampleMesageName -to user@example.edu -replace {'firstName': 'Zara', 'userName': 'zpara'}
~~~~

The user will then be sent an html based email.








