import json
import urllib.request, urllib.parse,urllib.error
import ssl


url = 'http://py4e-data.dr-chuck.net/comments_28334.json'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

file = urllib.request.urlopen(url, context=ctx)
data = file.read().decode()
print('Retrived', len(data), 'characters')
# try:
info = json.loads(data)
#
# print(json.dumps(info, indent=4))

total = 0
for data in info['comments']:
    total += int(data['count'])
print(total)
