
#!/bin/env python
 
import requests
import re

username = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'

url = 'http://%s.natas.labs.overthewire.org/' % username 

#cookies = {"loggedin" : "1"}

session = requests.Session()
response = session.post(url, data = {"secret" : "FOEIUWGHFEEUHOFUOIU", "submit" : "submit"}, auth = (username, password))
#request = requests.get(url, auth = (username, password))
content = response.text
print content
#print re.findall('natas4:(.*)', content)[0]


