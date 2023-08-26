def emp_sort_by_sal(emp_l, min_sal, max_sal):

    # putting a salary range filter on every employee
    # saving those employees in a List whose salary range is between the range given in a filter function
    # func lambda of filter arguments checks whether the range of the employee salary is acceptable
    matching_emp = filter(lambda emp: min_sal <= emp[2] <= max_sal, emp_l)

    """
    An alternative way to do the above filtering step is commented below
    Employees filtered based on pay range
    matching_emp = []
    for emp in emp_l:
        if min_sal <= emp[2] <= max_sal:
            # saving those employees in a List
            matching_emp.append(emp)
    """

    # sorting employee in salary order (largest first)
    # The sorted function sorts a list in ascending order by default, we reversed this behaviour for descending order by passing TRUE in argument reverse.
    # The key arguments provides a function which will be executed for each element of list, the return value of that func will be used to determine the order
    # func lambda take an emp tuple as input and returns the salary (thrid element of tuple), list is sorted based on emp salary
    sorted_emp = sorted(matching_emp, key=lambda emp: emp[2], reverse=True)

    # Display the results in a proper table
    if sorted_emp:
        print("{:<20} {:<20} {:<10}".format("Name", "Job Title", "Salary"))
        print("-" * 50)
        for emp in sorted_emp:
            print("{:<20} {:<20} {:<10}".format(emp[0], emp[1], emp[2]))
    else:
        print("No employees found in the given salary range.")

# User input to specifying the file name 
# only file name if file is placed in python project directory
#if file is in other then python project enter full path of the file
#e.g C:\Users\dell\Downloads\Course Python Folder\Data file for exercise 5.txt

filename = input("Enter the text filename: ") 
while True:
    try:
        f = open(filename, "r")
        break
    except FileNotFoundError:
        print("File not found. Please try again.")
        filename = input("Enter the text filename: ")
# employee list declared
emp_list = []
for line in f:
    # splitting the file line content on the bases of ","
    file_data = line.strip().split(",")
    name = file_data[0]
    job_title = file_data[1]
    salary = int(file_data[2])
    # Adding file content in a list
    emp_list.append((name, job_title, salary))

f.close()  # file close function

# Print the list of tuples (for verification purposes)
print(emp_list)

# Ask the user to supply a salary range and display the matching employees
while True:
    try:
        min_salary = int(input("Please enter the minimum salary: "))
        max_salary = int(input("Please enter the maximum salary: "))
        emp_sort_by_sal(emp_list, min_salary, max_salary)
    except ValueError:
        print("Invalid input. Please try again.")
    else:
        # User specified answer for Quit or Continue
        choice = input("Enter 'q' to quit, or press Enter to search for another salary range: ")
        if choice.lower() == "q":
            break

print("Goodbye!")