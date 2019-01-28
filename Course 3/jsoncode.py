import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()

data = html.decode()

info = json.loads(data)
comments = info["comments"]

count = 0
for comment in comments:
	number = comment["count"]
	count = count + int(number)

print(count)