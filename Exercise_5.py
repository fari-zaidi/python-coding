import numpy as np

# Getting user specified input file name
# enter file path if not in python project directory 
# e.g. C:\Users\dell\Downloads\Data file for exercise 5.txt
file_name = input("Enter input text file name: ")

# Open file and read number of students and coursework weighting
with open(file_name, 'r') as f:
    n, cw_weightage = map(int, f.readline().split())

# Initializing array of obtained marks with zeros
dt = np.dtype([('regnum', int), ('exam', float), ('coursework', float), ('overall', float), ('grade', 'U2')])
marks_obtain_array = np.array([(0, 0.0, 0.0, 0.0, '')] * n, dtype=dt)

# Read file line by line and populate marks array
for i, line in enumerate(open(file_name, 'r').readlines()[1:], 0):
    regnum, exam, coursework = map(float, line.split())
    overall = round((1 - cw_weightage / 100) * exam + (cw_weightage / 100) * coursework)
    if exam < 30 or coursework < 30:
        grade = 'F'
    elif overall >= 70:
        grade = '1'
    elif overall >= 50:
        grade = '2'
    elif overall >= 40:
        grade = '3'
    else:
        grade = 'F'
    marks_obtain_array[i] = (int(regnum), exam, coursework, overall, grade)

# Sort marks obtained array through overall mark, [::-1] will give descending order sort
marks_obtain_array = np.sort(marks_obtain_array, order='overall')[::-1]

# Output the sorted marks_obtain_array to file
output_file = input("Enter output file name: ")
with open(output_file, 'w') as f:
      print(marks_obtain_array, file=f)
    #To make output file more readable to user you can print through a for Loop, following is the commentd code for the same:
    # for line_element in marks_obtain_array:
    #     print(f"Regist.num.: {line_element[0]}, Exam Marks: {line_element[1]}, Coursework Marks: {line_element[2]}, Overall Marks: {line_element[3]}, Grade: {line_element[4]}", file=f)


# Calculate and output number of students with each grade and list of failed students
stud_first = np.count_nonzero(marks_obtain_array['grade'] == '1')
stud_second = np.count_nonzero(marks_obtain_array['grade'] == '2')
stud_third = np.count_nonzero(marks_obtain_array['grade'] == '3')
stud_failed = np.count_nonzero(marks_obtain_array['grade'] == 'F')
failed_regnum = [str(regnum) for regno in marks_obtain_array['regnum'][marks_obtain_array['grade'] == 'F']]
print(f"First class: {stud_first}\nSecond class: {stud_second}\nThird class: {stud_third}\nFailed: {stud_failed}")
print(f"Failed students: {', '.join(failed_regnum)}")