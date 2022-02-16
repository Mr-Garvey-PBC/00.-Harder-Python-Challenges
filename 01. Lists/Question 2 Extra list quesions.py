# Pseudocode

# initalise an empty list
# input = User names
# use a loop to keep ading names until 'end' is entered
# Find midpoint of list by dividing the length by 2
# If len of list is odd, then to turn decimal to whole number we will use
# int(midpoint), Floor division eg 11//5=5, round(value,number of decimal places)
# Slice the list in half using the midpoint value [0:midpoint]
# Print out sliced list

student_names=[]

user_in=str(input("Please enter sudents name or enter 'end' to exit: "))

while user_in.lower() != 'end':
    student_names.append(user_in)
    user_in=str(input("Please enter sudents name or enter 'end' to exit: "))
    # What happens if i use the append operation here instead of at the sart of the loop?

midpoint=(len(student_names)//2) # Set a Midpoint value as a whole number using floor division

# Conditions for how many elements to print
if len(student_names)%2==0:  # Condition for even number of elements
    print(student_names[0:midpoint])
else:
    print(student_names[0:4])
  