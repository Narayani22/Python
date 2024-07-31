# Types of function arguments
# 1 : Positional arguments
# 2 : Keyword arguments
# 3 : Default arguments
# 4 : Variable number of argumants

# 1 : Positional argument :-

def Information(Name, Age, Salary):
    print("Name is : ",Name)
    print("Age is : ",Age)
    print("Salary is : ",Salary)

Information("Amit",32,90000)

Information("Pooja",29,70000)

# 2 : Keyword arguments :-

Information(Age = 31, Salary = 78000, Name = "Sagar")