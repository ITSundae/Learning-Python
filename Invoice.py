#K. Davenport
#FOR COLLEGE
#<redacted> Invoice Generator
#A program that helps generate a friendly little (static) invoice for students after calculating books, lab fees, and tuition.

#Varibles that must be primed: bookCost (52.99), labFees (25), tuition (157.93*3), Total (does the maths)
bookCost = 52.99
labFees = 25.00
tuition = 157.93
total=(bookCost+labFees+tuition*3)
#We declare asterisk and dashes as a variable because we don't want to count out 50 of those things.
asterisk = "*" *50
dashes = "-" *50

#We're breaking this down into blocks for a bit of simplicity.
print(asterisk +
    "\n\t <redacted college name>" +
    "\n\t <redacted address>" +
    "\n\t <redacted city>")

print(dashes +
    "\n\t Product Name: \t Product Price:" +
    "\n\t Books:" + "\t\t $" + str(bookCost)+
    "\n\t Lab Fees:" + "\t $" + str(labFees)+
    "\n\t Tuition:" + "\t $" + str(tuition))

print(dashes +
    "\n\t\t\t Total:"
    "\n\t\t\t $", str(total))

print(dashes +
    "\n\n Thank you for being a <redacted college> student!" +
    "\n" + asterisk)
