
employee_file = open("employees.txt", "r")

# can we read the file
# print(employee_file.readable())

# print(employee_file.read())

# read individual line
# print(employee_file.readline())

# Add data to array
# print(employee_file.readlines())

for employee in employee_file.readlines():
    print(employee)

employee_file.close()

