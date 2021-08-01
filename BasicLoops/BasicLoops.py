
# Program list - If construct ( Do any 7 ) :
# Due Thursday(9 AM)
# 1. Write a PYTHON program that reads a value of n and check the
# number is zero or non zero value.

def NPowerFunctions():
    print("\n"*2)
    print("*" * 26)
    print("NPOWER TRAINING PROGRAM")
    print("IF CONSTRUCT")
    print("*" * 26)
    num = int(input("Enter a number "))
    if(num == 0):
        print("this is zero")
    else:
        print("Not a zero")

    # 2. Write a PYTHON program to find a largest of two numbers.
    snum1, snum2 = input("Enter  2 numbers(Find the bigger) ").split()
    num1 = int(snum1)
    num2 = int(snum2)
    if(num1 > num2):
        print("First number is greater")
    elif(num2 > num1):
        print("Second number is greater")
    else:
        print("There equal")

    # 3. Write a PYTHON program that reads the number and check the no is
    # positive or negative.
    num = int(input("Enter a number "))
    if(num > 0):
        print("This number is positive")
    else:
        print("This number is negative")

    # 4. Write a PYTHON program to check entered character is vowel or
    # consonant.
    vowels = ("a", "e", "i", "o", "u")
    letter = input("Enter a letter")
    found = False
    for vowel in vowels:
        if(letter == vowel):
            found = True
    if(found == True):
        print("This is a vowel")
    else:
        print("This is a consonant")



    # 5. Write a PYTHON program to evaluate the student performance
    sgrade = input("Enter grade(in percentages)")
    grade = float(sgrade)
    # If % is >=90 then Excellent performance
    if(grade >= 90):
        print("Excellent performance")
    # If % is >=80 then Very Good performance
    elif(grade >= 80):
        print("Very Good performance")
    # If % is >=70 then Good performance
    elif(grade >= 70):
        print("Good performance")
    # If % is >=60 then average performance
    elif(grade >= 60):
        print("average performance")
    # else Poor performance.
    else:
        print("Poor Performance")
    # 6. Write a PYTHON program to find largest of three numbers.
    numbers = input("Enter a 3 numbers(Find the bigger) ").split()
    maxnum = 0
    for snumber in numbers:
        number = int(snumber)
        if(number > maxnum):
            maxnum = number
    print("The Biggest number is ", maxnum)

    # 7. Write a PYTHON program to find smallest of three numbers
    numbers = input("Enter a 3 numbers(Find the smallest) ").split()
    minnum = int(numbers[0])
    for snumber in numbers:
        number = int(snumber)
        if(number < minnum):
            minnum = number
    print("The Smallest number is ", minnum)

    # 8.Write a PYTHON program to check whether number is even or odd.
    num = int(input("Enter a number "))
    if(num % 2 == 0):
        print("This number is even")
    else:
        print("This number is odd")

    # 9.Write a PYTHON program to check a year for leap year.
    year = int(input("Enter year "))

    if(year % 4 == 0 or year % 4 == 400  ):
        print("The year is a leap year (it has 366 days).")
    else: #
        print("The year is not a leap year (it has 365 days).")



    # 10. A company insures its drivers in the following cases:
    # In all the other cases, the driver is not insured.
    insured = False
    age = int(input("Whats ur age"))
    marriage = input("Are you married(Y or N)")
    gender = input("Whats your gender(M or F) ")
    # - If the driver is married.
    # - If the driver is unmarried, male and above 30 years of age.
    # - If the driver is unmarried, female and above 25 years of age.
    # - all handled in one condition but it can split apart
    # converted to upper incase user inputted lowercase
    if(marriage.upper() == 'Y' and age > 30 and gender.upper() == 'M' or marriage.upper() == 'N' and age > 25 and gender.upper() == 'F' ):
        insured = True
    if(insured == True):
        print("You are insured")
    else:
        print("Not insured")


#*****************************************************Code for (FOR CONSTRUCT)***********************************************************



def MathFunctions():
    import Math
    print("*" * 30)
    print("FOR LOOP MATH TRAINING PROGRAM")
    print("IF CONSTRUCT")
    print("*" * 30)
    # 1. Write a PYTHON program to print the natural numbers up to n
    numberofterms = int(input("Count up to what number: "))
    for number in numberofterms:
        print(number)
    # 2. Write a PYTHON program to print even numbers up to n
    numberofterms = int(input("Count up to what number: "))
    for number in  range(0,numberofterms):
        if number % 2 == 0 and number != 0:
            print(number)
    # 3. Write a PYTHON program to print odd numbers up to n
    numberofterms = int(input("Count up to what number: "))
    for number in  range(0,numberofterms):
        if number % 2 != 0 and number != 0:
            print(number)
    # 4. Write a PYTHON program to print sum of natural numbers up to n.
    total = 0
    numberofterms = int(input("Count up to what number: "))
    for number in  range(0,numberofterms + 1):
        total += number
    print(total)
    # 5. Write a PYTHON program to print sum of odd numbers up to n
    total = 0
    numberofterms = int(input("sum of all odd numbers up to what number: "))
    for number in  range(0,numberofterms + 1):
        if number % 2 != 0:
            total += number
    print(total)
    # 6. Write a PYTHON program to print sum of even numbers up to n
    total = 0
    numberofterms = int(input("sum of all even numbers up to what number: "))
    for number in  range(0,numberofterms + 1):
        if number % 2 == 0:
            total += number
    print(total)
    # 7. Write a PYTHON program to print natural numbers up to n in reverse
    # order.
    numberofterms = int(input("Count up to what number: "))
    for number in reversed(range(numberofterms + 1)):
        print(number)
    # 8. Write a PYTHON program to print Fibonacci series up to n
    #first set of numbers in fibonnacci sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,
    numberofterms = int(input("print Fibonacci series up to(This one was pretty cool): "))
    first_number = 0
    previous_number = 1
    print(first_number)
    print(first_number+previous_number)
    for number in range(numberofterms + 1):
        print(first_number + previous_number)
        temp = first_number
        first_number += previous_number
        previous_number = temp
    # 9. Write a PYTHON program find a factorial of given number.
    numberofterms = int(input("find a factorial of given number "))
    for number in reversed(range(numberofterms + 1)):
        print(number)
    # 10. Write a PYTHON program to check the entered number is prime or
    # not
    prime = True
    entered_number = int(input("check the entered number is prime or not: "))
    for number in  range(2,entered_number):
        if entered_number % number == 0:
            prime = False
    if prime == True:
        print("the entered number is prime")
    else:
        print("the entered number is not prime")

    # 11. Write a PYTHON program to find the sum of digits of given number
    total = 0
    numberofterms = list(input("find the sum of digits of given number: "))
    for snumber in  numberofterms:
        number = int(snumber)
        total += number
    print(total)
    # 12. Write a PYTHON program to check the entered number is
    # palindrome or not
    palindrome = True
    numberstring = list(input("check if the entered number is palindrome or not"))
    reversed_list = reversed(numberstring)
    for i in range(0,len(numberstring)):
        if(numberstring[i] != numberstring[-(i+1)]):
            palindrome = False
    if(palindrome == True):
        print("the entered number is palindrome")
    else:
        print("the entered number is not palindrome")
    # 13. Write a PYTHON program to reverse the given number.
    numberstring = list(input("reverse the given number "))
    reversed_list = reversed(numberstring)
    for i in range(0,len(numberstring)):
        print(numberstring[i], numberstring[-(i+1)])
    # 14. Write a PYTHON program to print the multiplication table
    entered_number = int(input("Print the multiplication table: "))
    print("Multiplication Table")
    for number in range(1,13):
        print(entered_number, " * ", number, " = ", entered_number * number)

    # 15. Write a PYTHON program to print the largest of n numbers
    numbers = input( "Pick some numbers ").split()
    print(numbers)
    max_number = 0
    for number in  numbers:
        actual_number = int(number)
        if(actual_number > max_number):
            max_number = actual_number
    print(str(max_number) +  " is the biggest number")
    # 16. Write a PYTHON program to print smallest of n numbers
    numbers = input("Enter a 3 numbers(Find the smallest) ").split()
    minnum = int(numbers[0])
    for snumber in numbers:
        number = int(snumber)
        if(number < minnum):
            minnum = number
    print("The Smallest number is ", minnum)


#************************************************************************Code for (WHILE LOOP CONSTRUCT)***********************************************************
# 1. Write a PYTHON program to print the natural numbers up to n

def MathFunctions2():
    n =  int(input("print the natural numbers up to n"))
    i = 0
    while(i <= n):
        print(i)
        i += 1

    # 2. Write a PYTHON program to print even numbers up to n
    n =  int(input("print the even natural numbers up to n"))
    i = 2
    while(i <= n):
        if( i % 2 == 0):
            print(i)
        i+=1
    # 3. Write a PYTHON program to print odd numbers up to n
    n =  int(input("print the odd natural numbers up to n"))
    i = 2
    while(i <= n):
        if( i % 2 != 0):
            print(i)
        i+=1
    # 4. Write a PYTHON program that prints 1 2 4 8 16 32 … n2
    n =  int(input("PYTHON program that prints n*2 up to this number"))
    i = 1
    while(i <= n):
        print( i * 2)
        i+= 1
    # 5. Write a PYTHON program to sum the given sequence
    # 1 + 1/ 1! + 1/ 2! + 1/3! + …. + 1/n!
    from fractions import Fraction
    n =  int(input("PYTHON program to sum the given sequence"))
    i = 1
    total = 0.0
    while(i <= n-1):
        print('1' + '/' + str(i) + ' + ', end='')
        i+= 1
        total += 1/i
    print('1' + '/' + str(n) + " = ")
    print(round(total,n))
    print(Fraction(round(total,n)).limit_denominator())
    # 6. Write a PYTHON program to compute the cosine series(didnt understand)
    # cos(x) = 1 – x2
    # / 2! + x4 / 4! – x6
    # / 6! + … xn
    # / n!
    # 7. Write a short PYTHON program to check weather the square root of
    # number is prime or not.
    prime = True
    entered_number = int(input("check the entered number is prime or not: "))
    squared_number = int(entered_number ** 0.5)
    for number in  range(2,squared_number):
        if squared_number % number == 0:
            prime = False
    if prime == True:
        print("the entered number is prime")
    else:
        print("the entered number is not prime")
    # 8. Write a PYTHON program to produce following design
    numberofterms = int(input("Produce this number of letters from A:"))
    # A B C
    # A B C
    # A B C
    numberofletters = int(input("Produce this number of letters from A:(no number greater than 26)"))
    h = 0
    alphabet = list(map(chr,list(range(65, 91))))
    while(h < numberofletters):
        print(alphabet[0:numberofletters])
        h+=1
    # 9. Write a PYTHON program to produce following design
    # A
    # A B
    # A B C
    # A B C D
    # A B C D E
    numberofletters = int(input("Produce this number of letters from A:(no number greater than 26)"))
    h = 0
    alphabet = list(map(chr,list(range(65, 91))))
    while(h < numberofletters):
        print(alphabet[0:h+1])
        h+=1

    # If user enters n value as 5
    # 10. Write a PYTHON program to produce following design
    # A B C D E
    # A B C D
    # A B C
    # A B
    # A
    numberofletters = int(input("Produce this number of letters from A:(no number greater than 26)"))

    h = 0
    alphabet = list(map(chr,list(range(65, 91))))
    while(h < numberofletters):
        print(alphabet[0:numberofletters-h])
        h+=1

    # (If user enters n value as 5)
    # 11. Write a PYTHON program to produce following design
    # 1
    # 1 2
    # 1 2 3
    # 1 2 3 4
    # 1 2 3 4 5
    numberofterms= int(input("Produce this number of numbers from 1:"))
    h = 1
    numbers = list(range(0, numberofterms+1))
    while(h <= numberofterms):
        print(numbers[1:h+1])
        h+=1

    # If user enters n value as 5
    # 12. Write a PYTHON program to produce following design
    # 1
    # 2 2
    # 3 3 3
    # 4 4 4 4
    # 5 5 5 5 5
    numberofterms= int(input("Produce this number of numbers from 1:"))
    h = 1
    i = 1
    while(h <= numberofterms):
        num = [i] * (h+1)
        print(num[1:h+1])
        h+=1
        i+=1
    # If user enters n value as 5
    numberofterms= int(input("Produce this number of numbers from 1:"))
    h = 1
    numbers = list(range(0, numberofterms+1))
    while(h <= numberofterms):
        print(numbers[1:h+1])
        h+=1

def Npowermenu():
    flag = 1
    valid = 1
      
    while(valid == 1):
        print("NPOWER MENU \nChoose a number")
        print("1. NPOWER TRAINING PROGRAM \n2. FORLOOPSPROGRAM \n3. WHILELOOPSPROGRAM")
        user_input = int(input("Choose a number between 1 and 3"))
        if(user_input == 0):
            print("Goodbye Thanks for playing")
            valid = 0
            flag = 0
        elif(user_input > 4 or user_input < 0):
            print(" ERROR Please choose a number between 1 and 3")
        else:
            valid = 1
            print("starting up program...")
            if(user_input == 1):
                NPowerFunctions()
                print("Thanks For Playing\n\n")
                valid = 1
            elif(user_input == 2):
                MathFunctions()
                print("Thanks For Playing\n\n")
                valid = 1
            else:
                MathFunctions2()
                print("Thanks For Playing\n\n")
                
Npowermenu()

    
