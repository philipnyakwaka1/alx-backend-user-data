#!/usr/bin/env python3
import base64
""" Main 1
"""
with open('buildings.PNG', 'rb') as f:
    data = f.read()

base64_encoding = base64.b64encode(data)
base64_string = base64_encoding.decode('ascii')
new_data = base64.b64decode(base64_string)

s = 'SG9sYmVydG9u'
en = base64.b64decode(s)
utf = en.decode('utf-8')
print(utf)