"""
BalancedParens.py
By: Christian Fuller

This file checks to see if parenthesis in a entered input is
balanced or unbalanced.
"""

from linkedstack import LinkedStack


def isBalanced(string):          
    """Returns True if parenthesis/brackets are balanced
    or False if unbalanced."""

    #Initiation of LinkedStack class
    s1 = LinkedStack()

    #This is a list of possible parenthesis assignments
    #The R1 and L1 are used as counters
    LParens = ['(', '[', '{']
    RParens = [')', ']', '}']
    R1 = 0
    L1 = 0

    #This for loop takes the inputed string and
    #then pushes the string onto the stack
    for i in string:
        if i in LParens:
            L1 += 1
            s1.push(i)
        elif i in RParens:
            if L1 == 0:
                return False
            R1 += 1
            locationR = RParens.index(i)
            #Peeking into the string list to verify
            locationL = LParens.index(s1.peek())
            #If equal, pop off the stack. Otherwise return false
            if locationL == locationR:
                s1.pop()
            else:
                return False
        #Here is where the comparison happens for balanced/unbalanced parens
        #Balanced = true, unbalanced = false
    if R1 == L1:
        return True
    else:
        return False
  

def main():
    while True:
        string = input("Enter an expression or Return to quit: ")
        if string == "":
            break
        elif isBalanced(string):
            print("The parentheses are balanced")
        else:
            print("The parentheses are not balanced ")
            

if __name__ == '__main__': 
    main()