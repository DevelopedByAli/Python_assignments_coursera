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

# Retrieving http://
serviceurl = "http://py4e-data.dr-chuck.net/geojson?"

# address
address = input('Enter location: ')
url = serviceurl + urllib.parse.urlencode({'address': address})

# print("Enter location:", address)

print('Retrieving', url)

uh = urllib.request.urlopen(url)

data = uh.read()
info = json.loads(data)
print('Retrieved', len(data), 'characters')

# print place id
print("Place id " + info['results'][0]['place_id'])

//////////// useful code \\\\\\\\\\\

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()
    # https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()

# Musical Track Database
# This application will read an iTunes export file in XML and produce a properly normalized database with this structure:

'''CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);'''

# If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

# You can use this code as a starting point for your application: http://www.py4e.com/code3/tracks.zip. 
# The ZIP file contains the Library.xml file to be used for this assignment.
# You can export your own tracks from iTunes and create a database, but for the database that you turn in for this assignment, 
# only use the Library.xml data that is provided.
# To grade this assignment, the program will run a query like this on your uploaded database and look for the data it expects to see:

'''SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3'''

import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue

    artist = lookup(entry, 'Artist')
    genre = lookup(entry, 'Genre')
    album = lookup(entry, 'Album')

    name = lookup(entry, 'Name')
    length = lookup(entry, 'Total Time')
    rating = lookup(entry, 'Rating')
    count = lookup(entry, 'Play Count')

    if artist is None or genre is None or album is None or name is None :
        continue

    print(name, artist, album, count, rating, length)

    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ?, ? )''',
        ( name, album_id, genre_id, length, rating, count ) )

    conn.commit()
