# Assignment number 14, Python for everybody, Coursera
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
