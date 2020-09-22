# Python for everybody assignements 
# assignment number 1 (2.1)

name = input("Enter your name")
print("Hello", name)

# assignment number 2 (2.2)

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
x = float(hrs)*float(rate)
print("Pay:", x)

# assignment number 3 (3.1)(using if/else statements (conditionals) first time in python)

hrs = input("Enter Hours:")
rate = input("Enter Rate")
h = float(hrs)
r = float(rate)
if h > 40 : pay = h * r
else : pay = h * r + 5 * 1.5 * r
print("Pay:", pay)
    
# Assignment number 4 (3.3)(using the if/elif/else conditionals)    

score = input("Enter Score between 0.0 and 1.0: ")
s = float(score)
if 0.0 <= s < 0.6:print ("F")
elif 0.6 <= s < 0.7:print("D")
elif 0.7 <= s < 0.8:print("C")
elif 0.8 <= s < 0.9:print("B")
elif 0.9 <= s < 1.0:print("A")
else:print("error")  
    
# Assignment number 5 (4.6)(Creating and using functions the first time during an assignment)  

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

#Assignment number 6 (5.2)(Creating and using loops (while, for) the first time during an assignemnt)
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
