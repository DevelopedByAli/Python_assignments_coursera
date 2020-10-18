# Using Python to Access Web Data course

# Assignment number 14, #Python for everybody, #Extracting Data With Regular Expressions, #Coursera
# Using regular expressions (The Regex for the first time)
# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

import re
name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_42.txt"
handle = open(name)
x = list()
for line in handle : 
  y = re.findall('[0-9]+',line)
  x = x + y
summe = 0
for i in x : 
  summe = summe + int(i)
print(summe)

# Assignment number 15, # Exploring the HyperText Transport Protocol

# You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.
  
  http://data.pr4e.org/intro-short.txt

Last-Modified: Sat, 13 May 2017 11:22:22 GMT
ETag: "1d3-54f6609240717"
Content-Length: 467
Cache-Control: max-age=0
Content-Type: text/plain

# Assignment number 16   # Scraping HTML Data with BeautifulSoup  
# In this assignment you will write a Python program to use urllib to read the HTML from the data files below, and parse the data, 
# extracting numbers and compute the sum of the numbers in the file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Inserting the link
link = input('Enter - ')
html = urllib.request.urlopen(link, context=ctx).read()
up = BeautifulSoup(html, "html.parser")

# Retrieve all of span tags
tags = soup('span')
summe = 0
count = 0
for tag in tags:
  summe = summe + int(tag.contents[0]) 
  count = count + 1 
print(summe)
print(count)

# Assignment number 17   # Following Links in HTML Using BeautifulSoup
# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
# The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, 
# scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times 
# and report the last name you find.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Collecting the data
link = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

#Retrieving the data
print('Retrieving: %s'% link)
for i in range(0,count) :
  html = urllib.request.urlopen(link, context=ctx).read()
  soup = BeautifulSoup(html, "html.parser")
  
  # Retrieve all of span tags
  tags = soup('a')
  pass = 0
  for tag in tags :
    pass = pass + 1
    if ps == line :
      print('Retrieving:' % str(tag.get('href',None)))
      link = str(tag.get('href',None))
      pass = 0
      break
    
# Assignment number 18   # Extracting data from XML    
# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, 
# compute the sum of the numbers in the file.
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_965682.xml (Sum ends with 55)   

# To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named 'count' with the following line of code:
  counts = tree.findall('.//count')

# Cod starts from here
import urllib.request as ur
import xml.etree.ElementTree as et 

url = input('Enter location: ')
# 'http://python-data.dr-chuck.net/comments_42.xml'

total_number = 0
summe = 0

print('Retrieving', url)
xml = ur.urlopen(url).read()
print('Retrieved', len(xml), 'characters')

tree = et.fromstring(xml)
counts = tree.findall('.//count')
for count in counts:
  summe += int(count.text)
  total_number += 1
  
print('Count:', total_number)  
print('Sum:', summe)

# sample output:
Enter location: http://py4e-data.dr-chuck.net/comments_965682.xml
Retrieving http://py4e-data.dr-chuck.net/comments_965682.xml
Retrieved 4232 characters
Count: 50
Sum: 2355
  
# Assignment number 19  # Extracting Data from JSON (javaScript Object Notation)
# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. 
# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, 
# compute the sum of the numbers in the file and enter the sum below:
# We provide two files for this assignment. 
# One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

  # Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
  # Actual data: http://py4e-data.dr-chuck.net/comments_965683.json (Sum ends with 64)

import urllib.request as ur
import json

link = input('Enter location: ')
data = ur.urlopen(link).read().decode('utf-8')
print('Retrieved: ', len(data), 'characters')
object = json.loads(data)

summe = 0
counts = 0

for comment in object["comments"]:
    summe += int(comment["count"])
    counts += 1
    
print('count', counts)
print('summe: ', summe)

# Assignment number 20  # Using the GeoJSON API

# Calling a JSON API

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
# API End Points

# To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

http://py4e-data.dr-chuck.net/json?
  
# This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. 
# If you visit the URL with no parameters, you get "No address..." response.
# To call the API, you need to include a key= parameter and provide the address that you are requesting as the address = parameter that is properly URL encoded using 
# the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py

# Make sure to check that your code is using the API endpoint is as shown above. You will get different results from the geojson and json endpoints so make sure 
# you are using the same end point as this autograder is using.

import urllib.request, urllib.parse, urllib.error
import json

