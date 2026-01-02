# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {
  'name': 'Jose',
  'school': 'Computing',
  'grades': (66, 77, 88)
}

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
  grades = data['grades']
  return sum(grades) / len(grades)

# print(average_grade(student))

#################################################################################################################



# # Implement the function below
# # Given a list of students (dictionaries), calculate the average grade of the classs
# # You must add all the grades of all the students together
# # You must also count how many grades there are in total in the entire list
# def average_grade_all_students(student_list):
#   total = 0
#   count = 0
#   for student in student_list:
#     total += sum(student["grades"])
#     count += len(student["grades"])
#     print(total, count)
#   return total / count

# students = [
#   {
#     'name': 'Jose',
#     'school': 'Computing',
#     'grades': (66, 77, 88)
#   }, 
#   {
#     'name': 'Tom',
#     'school': 'Computing',
#     'grades': (64, 91, 58)
#   },
#     {
#     'name': 'Bob',
#     'school': 'Computing',
#     'grades': (80, 97, 73)
#   }
# ]

# print(average_grade_all_students(students))