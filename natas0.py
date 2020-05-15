#!/bin/env python
 
import requests
import re

username = 'natas0'
password = 'natas0'

url = 'http://%s.natas.labs.overthewire.org' % username 

request = requests.get(url, auth = (username, password))
content = request.text
#print content.text
print re.findall('<!--The password for natas1 is (.*) -->', content)[0]
