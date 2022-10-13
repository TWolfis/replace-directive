# replace-emails
easily replace emails in nagios configuration


## usage 

```console
usage: replace-emails.py [-h] [-r] [-c] [-e, EMAIL]

Replace emails in /etc/nagios/generic/contacts.cfg prints out new
configuration to terminal

optional arguments:
  -h, --help            show this help message and exit
  -r, --replace         Force replacement of emails in
                        /etc/nagios/generic/contacts.cfg with the replacement
                        email
  -c, --current         Print out email addresses in
                        /etc/nagios/generic/contacts.cfg
  -e, EMAIL, --email EMAIL
                        Overwrite default replacement email with specified
                        email
```
