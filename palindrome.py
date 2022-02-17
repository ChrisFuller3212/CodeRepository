"""
File: palindrome.py
By:Christian Fuller
Project 7.2

"""

from arrays import Array
from arraystack import ArrayStack
from linkedstack import LinkedStack

def isPalindrome(string):          
    """Returns True if string is a palindrome
    or False otherwise."""
    
    #Instantiation of the class LinkedStack
    s1 = LinkedStack()

    #Exactly like ArrayStack, this for 
    #Loop takes the instantiation (s1) and 
    #Uses the push function from ArrayStack.
    for i in string:
        s1.push(i)

    #From there, I use another variable (j) and 
    #Convert the value of s1 to string. Then, I use
    #The pop function from the class. The logic after 
    #Compares the strings to see if the entered value
    #Is a palindrone. True is a palindrome, False otherwise.
    for i in string:
        j = str(s1.pop())
        if i != j:
            return False
    return True


def main():
    while True:
        string = input("Enter a string or Return to quit: ")
        if string == "":
            break
        elif isPalindrome(string):
            print("It's a palindrome")
        else:
            print("It's not a palindrome")
            

if __name__ == '__main__': 
    main()
