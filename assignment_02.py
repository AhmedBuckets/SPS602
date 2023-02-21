# Q1. What will the following code display?
numbers = [1, 2, 3, 4, 5]
print(numbers[1:-5])
#[] (empty list)
# Can you debug and fix the output? The code should return the entire list
print(numbers[0:])

# Q2. Design a program that asks the user to enter a store’s sales for each day of the
# week. The amounts should be stored in a list. Use a loop to calculate the total sales for
# the week and display the result.
week = []
for i in range(0,7):
	days_sales = int(input("Enter the day's sales: "))
	week.append(days_sales)

print(week)

sum=0 
for i in week:
	sum=sum+i

print(sum)

# Q3. Create a list with at least 5 places you’d like to travel to. Make sure the list isn’t in
# alphabetical order
# ● Print your list in its original order.
# ● Use the sort() function to arrange your list in order and reprint your list.
# ● Use the sort(reverse=True) and reprint your list.

travel_spots= ['Alaska', 'Iceland', 'Japan', 'Pakistan', 'Australia', 'Turkey']
print(travel_spots)

travel_spots.sort()
print(travel_spots)

travel_spots.sort(reverse=True)
print(travel_spots)


# Q4. Write a program that creates a dictionary containing course numbers and the room
# numbers of the rooms where the courses meet. The program should also create a
# dictionary containing course numbers and the names of the instructors that teach each
# course. After that, the program should let the user enter a course number, then it should
# display the course’s room number, instructor, and meeting time.

room_nums = {
	607:"A1",
	608:"A2",
	620:"B1",
	602:"B2",
	605:"C1" 
}

instructors = {
	607:"Doug Dimmadome",
	608:"Dimms Dale",
	620:"Dimma Dome",
	602:"Cosmo Greenhead",
	605:"Wanda Purplehair" 
}


course_nums = int(input("Enter a course num: "))
print("This class meets in room " + room_nums[course_nums] + " and is taught by professor: " + instructors[course_nums] )


# Q5. Write a program that keeps names and email addresses in a dictionary as
# key-value pairs. The program should then demonstrate the four options:
# ● look up a person’s email address,
# ● add a new name and email address,
# ● change an existing email address, and
# ● delete an existing name and email address.

instructors = {
	"Doug Dimmadome":"DDimmadome@gmail.com",
	"Dimms Dale":"DimmsDale@gmail.com",
	"Dimma Dome":"DDome@gmail.com",
	"Cosmo Greenhead":"greenhead@gmail.com",
	"Wanda Purplehair":"Purplehair@gmail.com" 
}

email_lookup = input("Enter the name whos email you would like to look up: ")
print(instructors[email_lookup])

name_add = input("Enter name to add: ")
email_add= input("Enter email to add: ")
instructors[name_add]=[email_add]
print(instructors)

name_mod = input("Enter name to modify: ")
email_mod= input("Enter email to modify: ")
instructors[name_mod]=[email_mod]
print(instructors)

name_del = input("Enter name to denlete: ")
del instructors[name_del]
print(instructors)






