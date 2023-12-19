employeeFile = open("employees.txt", "r") # r = read
print(employeeFile.readable()) # readable() = boolean
# print(employeeFile.read()) # read() = read all
# print(employeeFile.readline()) # readline() = read one line
# print(employeeFile.readline()) # readline() = read one line
# print(employeeFile.readlines()) # readlines() = read all lines and put them in a list
print(employeeFile.readlines()[1]) # readlines() = read all lines and put them in a list
employeeFile.close()