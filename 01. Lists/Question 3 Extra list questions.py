#Program name: Exercise 3 student marks
#Asks the user to enter a student name and the marks obtained on 10 weekly tests.
#Prints the top three and the bottom three marks

student_results=[]

student_name_input=str(input('Please enter the students name: '))

for i in range (1,11):
    student_results_input=int(input(f'Please enter students result for test {i}: '))
    student_results.append(student_results_input)

sortedMarks=sorted(student_results, reverse=True)

average_mark=sum(student_results)/10
print(f'{student_name_input} scored an average of {average_mark}')
print(f'{student_name_input}s 3 highest marks were:\n\t\t\t {sortedMarks[0:2]}')
print(f'{student_name_input}s 3 lowest marks were:\n\t\t\t {sortedMarks[-3:-1]}')