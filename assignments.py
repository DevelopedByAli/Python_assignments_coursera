# assignment number 1 (2.1)

name = input("Enter your name")
print("Hello", name)

# assignment number 2 (2.2)

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
x = float(hrs)*float(rate)
print("Pay:", x)

# assignment number 3 (3.1)

hrs = input("Enter Hours:")
rate = input("Enter Rate")
h = float(hrs)
r = float(rate)
if h > 40 : pay = h * r
else : pay = h * r + 5 * 1.5 * r
print("Pay:", pay)
    
# Assignment number 4 (3.3)    

score = input("Enter Score between 0.0 and 1.0: ")
s = float(score)
if 0.0 <= s < 0.6:print ("F")
elif 0.6 <= s < 0.7:print("D")
elif 0.7 <= s < 0.8:print("C")
elif 0.8 <= s < 0.9:print("B")
elif 0.9 <= s < 1.0:print("A")
          else:print("error")  
