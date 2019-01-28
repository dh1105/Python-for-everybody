import re

filename = "This file contains the actual data for your assign.txt"
handle = open(filename, 'r')

data = handle.read()

numbers = re.findall("[0-9]+", data)

count = 0
for number in numbers:
	count = count + int(number)

print(count)