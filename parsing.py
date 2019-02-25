import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = 'http://py4e-data.dr-chuck.net/comments_28333.xml'

#Ignore SSL Sertificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = urllib.request.urlopen(url)
tree = ET.parse(data)

# lst = tree.findall('comments/comment')

findSum = tree.findall('.//count')
total = 0
for count in findSum:
    total += int(count.text)
print('total:', total)
