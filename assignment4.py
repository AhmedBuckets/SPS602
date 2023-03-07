Q1: Create a class called BankAccount that has four attributes: bankname, firstname,
lastname, and balance.
The default balance should be set to 0.
In addition, create ...
● A method called deposit() that allows the user to make deposits into their balance.
● A method called withdrawal() that allows the user to withdraw from their balance.
● Withdrawal may not exceed the available balance. Hint: consider a conditional argument
in your withdrawal() method.
● Use the __str__() method in order to display the bank name, owner name, and current
balance.
● Make a series of deposits and withdrawals to test your class.
Q2: Create a class Box that has attributes length and width that takes values for length
and width upon construction (instantiation via the constructor).
In addition, create…
● A method called render() that prints out to the screen a box made with asterisks of
length and width dimensions
● A method called invert() that switches length and width with each other
● Methods get_area() and get_perimeter() that return appropriate geometric calculations
● A method called double() that doubles the size of the box. Hint: Pay attention to return
value here.
● Implement __eq__ so that two boxes can be compared using ==. Two boxes are equal if
their respective lengths and widths are identical.
● A method print_dim() that prints to screen the length and width details of the box
● A method get_dim() that returns a tuple containing the length and width of the box
● A method combine() that takes another box as an argument and increases the length
and width by the dimensions of the box passed in
● A method get_hypot() that finds the length of the diagonal that cuts through the middle
● Instantiate 3 boxes of dimensions 5,10 , 3,4 and 5,10 and assign to variables box1,
box2 and box3 respectively
● Print dimension info for each using print_dim()
● Evaluate if box1 == box2, and also evaluate if box1 == box3, print True or False to the
screen accordingly
● Combine box3 into box1 (i.e. box1.combine())
● Double the size of box2
● Combine box2 into box1