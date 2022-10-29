#Michael Hierrezuelo
#Auto Loan Calculator
#Introduction
print("Welcome To Michael's Auto Loan Calculator!")
print("Please Follow Next Steps And Input The Following To Get Started:")

#Name Entry
print("Let's Begin With Your Name!")
firstName = input("Enter First Name: ")
lastName = input("Enter Last Name: ")
fullName = firstName+" "+lastName
print(fullName)
print("Please Type Yes/Y Or No/N")

#Name Confirmation
nameConfirmation = input("Is This Correct? ")
if (nameConfirmation.upper() == "Y" or nameConfirmation.upper() == "Yes"):
    print("Thank You!")
elif (nameConfirmation.upper() == "N" or nameConfirmation.upper() == "No"):
    print("Return Back To Line 7")

#Birthday Entry
print("Please Enter Your Birthday (In Format: MMDDYYYY): ")
birthMonth = input("Enter Birth Month: ")
birthDay = input("Enter Birth Day: ")
birthYear = input("Enter Birth Year: ")
fullBirthday = (birthMonth+"/"+birthDay+"/"+birthYear)
print(fullBirthday)
print("Please Type Yes/Y Or No/N")

#Birthday Confirmation
dateOfBirthConfirmation = input("Is This Correct? ")
if (dateOfBirthConfirmation.upper() == "Y" or dateOfBirthConfirmation.upper() == "Yes"):
    print("Thank You!")
elif (dateOfBirthConfirmation.upper() == "N" or dateOfBirthConfirmation.upper() == "No"):
    print("Return Back To Line 22")

#Loan Details Entry
loanAmount = input("Enter Loan Amount: $")
downPayment = input("Down Payment: $")
loanAPR = input("Enter Loan Annual Percentage Rate (APR): ")
loanTerm = input("Enter Loan Term (In Months): ")
taxPercentage = input("Enter Tax Percentage: ")
print("Please Review: Your Loan Amount Of $"+loanAmount, "With A Down Payment Of $"+downPayment, "For A Term Of ", loanTerm, "Months At An Annual Percentage Rate Of", loanAPR+"% And The Tax Percentage Of", taxPercentage+"%")
print("Please Type Yes/Y Or No/N")

#Loan Details Confirmation
loanDataInformation = input("Is This Correct? ")
if (loanDataInformation.upper() == "Y" or loanDataInformation.upper() == "Yes"):
    print("Thank You!")
elif (loanDataInformation.upper() == "N" or loanDataInformation.upper() == "No"):
    print("Return Back To Line 38")
    
#In Progress...
#print("Calculating...")
#afterDownPayment = loanAmount - downPayment
#annualInterestRate = float(loanAPR / 100)
#totalWithAPR = afterDownPayment * (1 +annualInterestRate)
#monthlyTotalBeforeTax = annualInterestAmount / 12
#taxRate = float(taxPercentage / 100)
#monthlyTotalAfterTax = monthlyTotalBeforeTax * (1 + taxRate)
print("Done!")
#print("Your Monthly Payment: ", monthyTotalAfterTax)
print("Would You Like To Edit/Make Changes?")
restartCalculator = input("Yes or No? ")
if (restartCalculator.upper() == "Y" or restartCalculator.upper() == "Yes"):
    print("Thank You!")
elif (restartCalculator.upper() == "N" or restartCalculator.upper() == "No"):
    print("Return Back To Line 7")
#In Progress...

#Additional Requirements: 

#print("Michael", end= "Hello") = MichaelHello (Adds Whatever Is Assigned For "end" To The End Of The Printed Statement?)
#print("Hello", "Michael", sep= " Add Something Here ") = Hello Add Something Here Michael (Replaces The "," To Whatever Is Assigned For "sep")
#print(5 ** 2) = 5^(2) = 25 (Power/Exponent)
#print(5 * 5) = 25 (Multiplication)
#print(25 / 5) = 5 (Division)
#print(26 % 5) = 1 (The Remainder When Divided)
#print(26 // 5) = 5 (Divide Without Showing Remainder)
#print(5 + 5) = 10 (Addition)
#print(5 - 5) = 0 (Subtraction)
#print("Hello" * 5) = HelloHelloHelloHelloHello (Types "Hello" 5 Times Together)
#print ("Hello"+"Michael") = HelloMichael (Brings The Two Strings Together)