"""
Write a program that will take a number (Integers only) and return a statement that let will the user know if its even or odd
"""
x=int(input('Please enter a number: '))
if x%2 == 0:
    print('Your number is even.')
else:
    print('Your number is odd.')