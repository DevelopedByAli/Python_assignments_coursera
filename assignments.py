# Python for everybody assignements 
# assignment number 1 (2.1)

name = input("Enter your name")
print("Hello", name)

# assignment number 2 (2.2)

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
x = float(hrs)*float(rate)
print("Pay:", x)

# assignment number 3 (3.1) (using if/else statements (conditionals) first time in python)

hrs = input("Enter Hours:")
rate = input("Enter Rate")
h = float(hrs)
r = float(rate)
if h > 40 : pay = h * r
else : pay = h * r + 5 * 1.5 * r
print("Pay:", pay)
    
# Assignment number 4 (3.3) (using the if/elif/else conditionals)    

score = input("Enter Score between 0.0 and 1.0: ")
s = float(score)
if 0.0 <= s < 0.6:print ("F")
elif 0.6 <= s < 0.7:print("D")
elif 0.7 <= s < 0.8:print("C")
elif 0.8 <= s < 0.9:print("B")
elif 0.9 <= s < 1.0:print("A")
else:print("error")  
    
# Assignment number 5 (4.6) (Creating and using functions the first time during an assignment)  

def computepay(h,r) : 
    if h <= 40 : pay = h * r
    else : pay = h * r + 5 * 0.5 * r
    return pay
hrs = input("Enter Hours:")
hs = float(hrs)
rate = input("Enter Rate:")
rt = float(rate)
p = computepay(hs,rt)
print("Pay",p)

#Assignment number 6 (5.2) (Creating and using loops (while, for) the first time during an assignemnt)
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try:
        numb = int(num)
    except:
        print("Invalid input")
        continue
    if smallest is None : smallest = numb
    elif numb < smallest : smallest = numb
    
    if largest is None : largest = numb 
    elif numb > largest : largest = numb
print("Maximum is", largest)
print("Minimum is", smallest)

# From here I completed the first course and started the second one named "Python Data Structures"

# Assignment number 7 (6.5) (Started using Python built-in functions and methods)

text = "X-DSPAM-Confidence:    0.8475";
opos = text.find('0')
npos = text.find('5')
spos = text[opos : npos + 1]
result = float(spos)
print(result)

# Assignment number 8 (7.1) (Printing the text words from a given file)
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip().upper()
    print(line)

# Assignment number 9 (7.2) (Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
#  Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.)

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
sm = 0.0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    sm = sm + float(line[20:])
    count = count + 1
print("Average spam confidence:", sm / count)    

# Assignment number 10 (8.4) (According to a theoty of lists)

# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.split()
    for word in line:
        if not word in lst:
             lst.append(word)
lst.sort() 
print(lst)

# Assignment number 11 (8.5)
# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('From') : continue

