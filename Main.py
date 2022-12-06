# Auto Loan Calculator
# __author__ == Michael Hierrezuelo

def main():
    # Definitions
    def name_confirmation():
        """
        Confirm Inputted Name
        :return: Yes/No
        """
        yes = ["Yes", "Y", "yes", "y"]
        no = ["No", "N", "no", "n"]
        question = input("Is This Correct? Y or N? ")
        if question in yes:
            print("Thank You!")
            return True
        if question in no:
            print("Please Try Again...")
            firstName = input("Enter First Name: ")
            lastName = input("Enter Last Name: ")
            fullName = firstName + " " + lastName
            print(fullName)
            name_confirmation()
        else:
            print("Please Use 'Y' Or 'N'")
            name_confirmation()


    def birthday_confirmation():
        """
        Confirm Inputted Birthday
        :return: Yes/No
        """
        yes = ["Yes", "Y", "yes", "y"]
        no = ["No", "N", "no", "n"]
        question = input("Is This Correct? Y or N? ")
        if question in yes:
            print("Thank You!")
            return True
        if question in no:
            print("Please Try Again...")
            birthMonth = input("Enter Birth Month: ")
            birthDay = input("Enter Birth Day: ")
            birthYear = input("Enter Birth Year: ")
            fullBirthday = (birthMonth + "/" + birthDay + "/" + birthYear)
            print(fullBirthday)
            birthday_confirmation()
        else:
            print("Please Use 'Y' Or 'N'")
            birthday_confirmation()


    def loan_data_confirmation():
        """
        Confirm Inputted Loan Data
        :return: Yes/No
        """
        yes = ["Yes", "Y", "yes", "y"]
        no = ["No", "N", "no", "n"]
        question = input("Is This Correct? Y or N? ")
        if question in yes:
            print("Thank You!")
            return True
        if question in no:
            print("Please Try Again...")
            loanAmount = int(input("Please Enter The Amount On The Loan: $"))
            downPayment = int(input("Down Payment?: $"))
            loanAPR = float(input("Enter Loan Annual Percentage Rate (APR): "))
            loanTerm = int(input("Enter Loan Term (In Months): "))
            taxPercentage = float(input("Enter State Tax Percentage: "))
            print("Loan Amount: $", loanAmount, sep="")
            print("Down Payment: $", downPayment, sep="")
            print("Loan Term:", loanTerm, "Month(s)")
            print("Annual Percentage Rate: ", loanAPR, "%", sep="")
            print("State Tax Percentage: ", taxPercentage, "%", sep="")
            loan_data_confirmation()
        else:
            print("Please Use 'Y' Or 'N'")
            loan_data_confirmation()


    def reset_calculator():
        """
        Reset The Calculator Program
        :return: Yes/No
        """
        yes = ["Yes", "Y", "yes", "y"]
        no = ["No", "N", "no", "n"]
        question = input("Reset Calculator? ")
        if question in yes:
            print("Resetting...")
            main()
        if question in no:
            print("Thank You For Using Michael's Auto Loan Calculator! :)")
        else:
            print("Please Use 'Y' Or 'N'")
            reset_calculator()


    # Introduction
    print("Welcome To Michael's Auto Loan Calculator!")
    print("Please Follow Next Steps And Input The Following To Get Started: ")

    # Name Entry
    print("Let's Begin With Your Name!")
    firstName = input("Enter First Name: ")
    lastName = input("Enter Last Name: ")
    fullName = firstName + " " + lastName
    print(fullName)

    # Name Confirmation
    name_confirmation()

    # Birthday Entry
    print("Now Let's Confirm Your Date Of Birth")
    print("Please Enter Your Birthday Using Digits (MM/DD/YYYY)")
    birthMonth = input("Enter Birth Month: ")
    birthDay = input("Enter Birth Day: ")
    birthYear = input("Enter Birth Year: ")
    fullBirthday = (birthMonth + "/" + birthDay + "/" + birthYear)
    print(fullBirthday)

    # Birthday Confirmation
    birthday_confirmation()

    # Loan Details Entry
    print("Now Let's Get Started...")
    loanAmount = int(input("Please Enter The Amount On The Loan: $"))
    downPayment = int(input("Down Payment?: $"))
    loanAPR = float(input("Enter Loan Annual Percentage Rate (APR): "))
    loanTerm = int(input("Enter Loan Term (In Months): "))
    taxPercentage = float(input("Enter State Tax Percentage: "))
    print("Loan Amount: $", loanAmount, sep="")
    print("Down Payment: $", downPayment, sep="")
    print("Loan Term:", loanTerm, "Month(s)")
    print("Annual Percentage Rate: ", loanAPR, "%", sep="")
    print("State Tax Percentage: ", taxPercentage, "%", sep="")

    # Loan Details Confirmation
    loan_data_confirmation()

    print("Calculating...")

    afterDownPayment = loanAmount - downPayment
    taxRateDecimal = float(taxPercentage / 100)
    annualTotalAfterTax = afterDownPayment * (1.0 + taxRateDecimal)
    monthlyTotalAfterTax = annualTotalAfterTax / 12

    annualInterestRateDecimal = float(loanAPR / 100)
    annualTotalWithAPR = annualTotalAfterTax * (1.0 + annualInterestRateDecimal)
    monthlyTotalWithAPR = annualTotalWithAPR / 12
    print("Done!")
    print("Your Monthly Payment: ", monthlyTotalWithAPR)

    # Restart Calculator?
    reset_calculator()


main()

# Sprint 1 Additional Requirements:

# print("Michael", end= "Hello") = MichaelHello (Adds Whatever Is Assigned For "end" To The End Of The Printed
# Statement?)
# print("Hello", "Michael", sep= " Add Something Here ") = Hello Add Something Here Michael (Replaces The "," To
# Whatever Is Assigned For "sep")
# print(5 ** 2) = 5^(2) = 25 (Power/Exponent)
# print(5 * 5) = 25 (Multiplication)
# print(25 / 5) = 5 (Division)
# print(26 % 5) = 1 (The Remainder When Divided)
# print(26 // 5) = 5 (Divide Without Showing Remainder)
# print(5 + 5) = 10 (Addition)
# print(5 - 5) = 0 (Subtraction)
# print("Hello" * 5) = HelloHelloHelloHelloHello (Types "Hello" 5 Times Together)
# print ("Hello"+"Michael") = HelloMichael (Brings The Two Strings Together)


# Sprint 2 Additional Requirements:

# Shortcut Operators: x += 1 is the same (==) as x = x+ 1
# x == 1 means that the x must actually equal the same value as 1
# x != 2 means x must not actually equal to one
# x < 2 would make this True since 1 < 2
# Boolean: "and" is a "conditional" word used to make sure it goes for both "this" condition and "that" condition
# Boolean: "not" is also a conditional word used to make sure it is "not" meeting that specific condition(s)
# "While" is a Loop word that continues over and over usually for unknown amount of responses in the input
#for, in, range
#
#for i in range(1,101,2):
#    print(x)

