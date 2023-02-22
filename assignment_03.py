# Q1: Write a program that prompts the user for a meal: breakfast, lunch, or dinner. Then using if statements 
# and else statements print the user a message recommending a meal. For example, if the meal was breakfast, you could say something like, “How about some bacon and eggs?”
# The user may enter something else in, but you only have to respond to breakfast, lunch, or dinner.
meal_name = input("Enter a meal name: ")

if meal_name == "Breakfast":
   print("How about an omelete?")
elif meal_name == "Lunch":
   print("How about a salad?")
elif meal_name == "Dinner":
   print("How about some salmon?")
else: 
   print("Please enter Breakfast, Lunch, or Dinner.")

# Q2: The mailroom has asked you to design a simple payroll program that calculates a student employee’s gross pay, 
# including any overtime wages. If any employee works over 20 hours in a week, the mailroom pays them 1.5 times their regular hourly pay rate for all hours over 20. 
# You should take in the user’s input for the number of hours worked, and their rate of pay.
hours_worked = int(input("Enter hours worked: "))
pay_rate= int(input("Enter rate of pay: "))

if hours_worked >20:
   print("Total pay is: " + str((20*pay_rate) + ((hours_worked%20) * (1.5*pay_rate)) ))
else:
   print("Total pay is: " + str(hours_worked*pay_rate) )



# Q3: Write a function named times_ten. The function should accept an argument and display the product of its argument multiplied times 10.
def times_ten(x):
   print(x*10)

times_ten(5)


# SQ4: Find the errors, debug the program, and then execute to show the output.

# def main()
#       Calories1 = input( "How many calories are in the first food?")
#       Calories2 = input( "How many calories are in the first food?")
#       showCalories(calories1, calories2)

# def showCalories()   
#    print(“The total calories you ate today”, format(calories1 + calories2,.2f))

def showCalories(Calories1, Calories2):   
   print("The total calories you ate today: ", str(Calories1 + Calories2))

def main():
      Calories1 = int(input( "How many calories are in the first food?"))
      Calories2 = int(input( "How many calories are in the second food?"))
      showCalories(Calories1, Calories2)

if __name__ == "__main__":
   main()


# Q5: Write a program that uses any loop (while or for) that calculates the total of the following series of numbers:
#          1/30 + 2/29 + 3/28 ............. + 30/1
sum=0
for i in range(1,31):
   print(str(i) + "/" + str(31-i) )
   sum = sum + (i/(31-i))

print(sum)
#93.84460105853213


# Q6: Write a function that computes the area of a triangle given its base and height.
# The formula for an area of a triangle is:
# AREA = 1/2 * BASE * HEIGHT

# For example, if the base was 5 and the height was 4, the area would be 10.
# triangle_area(5, 4)   # should print 10

def triangle_area(b,h):
   area=1/2 * b * h 
   print("The area of the triange is: " + str(area))

triangle_area(5, 4)   # should print 10
