import re

number = str(raw_input('Put a phone number in crumbo>'))

search = re.search(r'\d{5}', number, re.M|re.I)

if search:
    print 'yes'
else:
    print 'no'
