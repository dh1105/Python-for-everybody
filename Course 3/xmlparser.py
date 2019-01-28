import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()

data = html.decode()

tree = ET.fromstring(data)
lst = tree.findall("comments/comment")

count = 0
for items in lst:
	number = items.find("count").text
	count = count + int(number)

print(count)