"""This program takes in a credit card number from the user and determines if it's valid.
Project name: creditCard.py
File name: project7
Created by: James Lawson and Beth Ann Townsend
"""

#math is imported
import math



def main():
    #the credit card number is inputted from the user
    number = input("Enter the card number: ")

    #function is called
    isValid(number)
    

def isValid(number):
    #if the credit card number is too short or too long, false is returned and the message is printed
    if len(number) < 13 or len(number) > 16:
        print("This card is invalid because it is too short or too long")
        return False
    totalSum = 0
    totalAllEven = 0
    totalAllOdd = 0
    totalAllEven = sumOfDoubleEvenPlace(number, totalAllEven)
    totalAllOdd = sumOfOddPlace(number, totalAllOdd)
    #the total sum of the odd and even values is calculated
    totalSum = totalAllOdd + totalAllEven
    #value of total sum is printed
    print("totalSum: ", totalSum)
    #value of totalSum % 10 is printed
    print("totalSum % 10: ", totalSum % 10)

    #if the prefix matches valid credit card prefixes, pass, if not, print the following statement and return False
    if prefixMatched(number, "4") or prefixMatched(number, "5") or prefixMatched(number, "37") or prefixMatched(number, "5") or prefixMatched(number, "6"):
        pass
    else:
        print("This card does not start with the right numbers")
        return False

    if True:
        #if the total sum is divisable by 10 with 0 remainder, the card is valid
        if totalSum % 10 == 0:
            print("You have a valid card!!!")
            return True
        else:
            print("This card is invalid, numbers do not divide by 10")
            return False

#this function doubles all of the numbers in the even places and then sums them
def sumOfDoubleEvenPlace(number, totalAllEven):
    #string is iterated through, skipping by 2
    for index in range(len(number) - 2, -1, -2):
        evenPlace = int(number[index])
        #values in the even places are doubled
        evenPlace = evenPlace * 2
        doubleDigitTotal = getDigit(str(evenPlace))
        #values are summed
        totalAllEven += doubleDigitTotal
    #value is printed
    print("totalAllEven: ", totalAllEven)
    #value is returned
    return totalAllEven

#if the length of the string is greater or equal to 2, both digits are summed
def getDigit(evenPlace):
    if len(str(evenPlace)) >= 2:
        return int(evenPlace[0]) + int(evenPlace[1])
    else:
        return int(evenPlace)

#this function sums all of the numbers in odd places
def sumOfOddPlace(number, totalAllOdd):
    #string is iterated through, skipping by 2
    for index in range(len(number) - 1, -1, -2):
        oddPlace = int(number[index])
        oddTotal = (oddPlace)
        #values are summed
        totalAllOdd += oddTotal
    #value is printed
    print("totalAllOdd: ",totalAllOdd)
    #value is returned
    return totalAllOdd

#the prefix is returned
def getPrefix(number, k):
    if len(number) > k:
        return number[:k]
    else:
        return number

#the prefix is checked for matches
def prefixMatched(number, d):
    newNumber = getPrefix(number, len(d))
    if newNumber == d:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
