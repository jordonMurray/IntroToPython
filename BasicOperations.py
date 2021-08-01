# 1. Write a Python program to solve (x + y) * (x + y)
print("=" * 21)
print("NPOWER PYTHON PROGRAM")
print("=" * 21)
x, y = input("Enter a two value: ").split()
print(" The answer is", (int(x) +  int(y)) * (int(x) +  int(y)))

# Test Data : x = 4, y = 3
# 2. Write a Python program to parse a string to Float or Integer.
word = input("Enter a number: ")
if(word.isnumeric() == True):
    print ("This is Int version fo your string ", int(word))
    print ("This is Float version fo your string ", float(word))
else: print("Come on man enter a number")
# 3. Write a Python program to find the sum of the first n positive integers.
numbers = input( "Pick some numbers(even negative) ").split()
print(numbers)
sum = 0
for number in  numbers:
    actual_number = int(number)
    if(actual_number > 0):
        sum += actual_number
print(str(sum) +  " is the sum")
# 4. Write a Python program to convert the distance (in feet) to inches, yards,
# and miles
unit = input(" How many feet")
print("This is " , int(unit) * 12 , " feet" )
print("This is " ,float(unit) * .33 , "yard" + "People still use yards?")

# 5. Write a Python program to convert all units of time into seconds
unit = input(" How many? (sec,min,hr)")
number = input("Give me a number")
if unit == "sec":
    print("This is ", float(number) / 60," minutes")
    print("This is ", float(number) / 3600," hr")
elif unit == "min":
    print("This is ", float(number) * 60 + " seconds")
    print("This is ", float(number) / 60 , + " hr")
elif unit == "hr":
    print("This is ", float(number) * 3600 + " seconds" )
    print("This is ", float(number) * 60  , + " min")
else:
    print("done")

# 6. Write a Python program to convert seconds to day, hour, minutes and
# seconds.
unit = input(" Second converter in (secs) Enter number")
print("This is ", int(unit)/86400, " days")
print("This is ", float(unit )/ 3600  , " hr")
print("This is " , float(unit )/ 60  , " minutes")
print("This is " , int(unit) , " seconds :o" )
# 7. Given variables x=30 and y=20, write  a Python program to print
# "30+20=50"
x, y = input("Enter two values: ").split()
print(x , " + " , y, " = " , int(x) + int(y))
# 8. Write a Python program to perform an action if a condition is true. Given a
# variable name, if the value is 1, display the string "First day of a Month!"
# and do nothing if the value is not equal.
day = input("Enter a number between 1 and 7")
if day == '1':
    print("Monday")
elif day == '2':
    print("Tuesday")
elif day == '3':
    print("Wednesday")
elif(day == '4'):
    print("Thursday")
elif(day == '5'):
    print("Friday")
elif(day == '6'):
    print("Saturday")
elif(day == '7'):
    print("Sunday")
# 9. Write a Python program to check whether variable is of integer or string
word = input("Enter something: ")
if(word.isnumeric() == True):
    print("This is a number ")
else:
    print(" it is a string")
# 10. Write a Python function to find the maximum and minimum numbers
# from a sequence of numbers
numbers = input( "Pick some numbers ").split()
print(numbers)
max_number = 0
for number in  numbers:
    actual_number = int(number)
    if(actual_number > max_number):
        max_number = actual_number
print(str(max_number) +  " is the biggest number")
