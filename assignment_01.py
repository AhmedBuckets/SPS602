#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95
 
# Get the test scores.
test1 = float(input('Enter the score for test 1: '))
test2 = float(input('Enter the score for test 2: '))
test3 = float(input('Enter the score for test 3: '))
# Calculate the average test score.
average = (test1 + test2 + test3) / 3
# Print the average.
print('The average score is', average)
# If the average is a high score,
# congratulate the user.
if average >= HIGH_SCORE:
    print('Congratulations!')
    HIGH_SCORE= average
print('That is a great average!')

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 
length_1 = float(input('Enter the length for rectangle 1: '))
width_1 = float(input('Enter the width for rectangle 1: '))

print("The area of rectangle 1 is: " + str(length_1*width_1))

length_2 = float(input('Enter the length for rectangle 2: '))
width_2 = float(input('Enter the width for rectangle 2: '))

print("The area of rectangle 1 is: " + str(length_2*width_2))

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"

name = input('Please enter your first name: ')
age = float(input('Please enter your age: '))
print('Happy birthday ' + name + '! You are ' + str(age) + ' years old today!')
