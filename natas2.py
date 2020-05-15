
#!/bin/env python
 
import requests
import re

username = 'natas2'
password = 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'

url = 'http://%s.natas.labs.overthewire.org/files/users.txt' % username 

request = requests.get(url, auth = (username, password))
content = request.text
#print content
print re.findall('natas3:(.*)', content)[0]


