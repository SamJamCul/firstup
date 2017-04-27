import re

number = str(raw_input('Enter a phone number plox>'))

#print (re.split(r'(s*)', 'here are some words'))

#print (re.split(r'[a-f][a-f]', 'adsASDFASDJIaf GRESGJGfjiovjarvlaij',
#    re.I|re.M))

print (re.findall(r'\d{1,4}\s\w+\s\w+\.', 'ocinwasdfae324 main st.asdfjaislregja'))
