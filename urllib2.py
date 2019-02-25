import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_28331.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())
tags = soup('span')
total = 0
for tag in tags:
    number = tag.contents[0]
    total = total + int(number)
print(total)
# retrieve all of anchor tags
# tags = ('span')
# for tag in tags:
#     print(tag.get('class', None))
