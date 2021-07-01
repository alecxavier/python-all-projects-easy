import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

990:123:1234
'''

sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r"\d\d\d[*:]\d\d\d[*:]\d\d\d\d")
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

 

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

domain = re.compile(r"[^https://][^www.?][a-zA-Z]+\.(com|gov)")
find_content = domain.finditer(urls)
for i in find_content:
    print(i)

