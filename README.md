# replace-emails
View and mass replace directives in nagios configuration files

## usage 

```console
usage: replace-directive.py [-h] [-r, REPLACEMENT] [-f, FILE] [-w] directive

Find and/or Replace directives in /etc/nagios/generic/contacts.cfg by default
print values for found directives for possible directives take a look at https
://assets.nagios.com/downloads/nagioscore/docs/nagioscore/3/en/objectdefinitio
ns.html

positional arguments:
  directive             Print out found matches of directive

optional arguments:
  -h, --help            show this help message and exit
  -r, REPLACEMENT, --replacement REPLACEMENT
                        Overwrites directive values with specified replacement
  -f, FILE, --file FILE
                        Look for directive in file, default file is
                        /etc/nagios/generic/contacts.cfg
  -w, --write           Overwrite directive with replacement directive
                        replacement

```
