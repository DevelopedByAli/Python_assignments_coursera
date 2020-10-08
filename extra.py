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
    
    
    
  
  
