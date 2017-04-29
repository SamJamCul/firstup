import re

number = str(raw_input('Put a phone number in crumbo>'))

search = re.search(r'\d{3}\s\d{4}\s\d{4}', number, re.M|re.I)

if search:
    print 'yes'
else:
    print 'no'
