#K. Davenport
#FOR COLLEGE
#A very simple calculator
#This program asks for what kind of arithmetic we're going to use, then asks the user for 2 different numbers to calculate.

print("Hello! I'm a simple program that will calculate two different numbers for you. Let's get started.")
arithmetic = input("Would you like to <add>, <subtract>, <multiply>, or <divide> today? ")

#Decision making occurs here to determine what kind of math we're doing today.
#If the user input something invalid, the program asks the user to input
#something else. It will loop until something valid is input.

#It's worth mentioning that NinjaJc01 of TryHackMe saved my brains on this one because I wanted to do something different.
#I tried "while arithmetic != ('add' or 'subtract' or 'multiply' or 'divide'):" at first and it functioned, but did not check the other 3 statements. He suggested using a "not in []" statement, which ended up fixing the issue.
#Also if I wanted to do what I originally wanted to do, it would functionally look like "while (arithmetic != 'add') or (arithmetic != 'subtract') or (arithmetic != 'multiply') or (arithmetic != 'divide')"
#So that's pretty cool and very gross. Cool fax for people to read about.
while not arithmetic in ["add", "subtract", "multiply", "divide"]:
    arithmetic = input("That's not a valid statement. You cannot calculate two numbers using <" + arithmetic + ">. Please select from <add>, <subtract>, <multiply>, or <divide>. ")

print("That sounds great! We're going to" , arithmetic , "today!")

#We're going to ask our user for the numbers they want to use.
firstNumber = input("Please input your first number. ")
firstNumber = float(firstNumber)
secondNumber = float(input("Thanks. Input your second number. "))

#Here the magic happens as we do the math and print appropriately.
if arithmetic == "add":
    total = firstNumber + secondNumber
    print("Okay. I'm done calculating. " , firstNumber , "+" , secondNumber , "=" , total)
elif arithmetic == "subtract":
    total = firstNumber - secondNumber
    print("Okay. I'm done calculating." , firstNumber , "-" , secondNumber , "=" , total)
elif arithmetic == "multiply":
    total = firstNumber * secondNumber
    print("Okay. I'm done calculating." , firstNumber , "*" , secondNumber , "=" , total)
elif arithmetic == "divide":
    total = firstNumber / secondNumber
    print("Okay. I'm done calculating." , firstNumber , "/" , secondNumber , "=" , total)
