'''Problem Statement   :
Create an object-oriented program that allows you to enter data for customers and employees.
Problem Details
Create a Person class that provides attributes for first name, last name, and email address.
This class should provide a property or method that returns the person’s fullname.
Create a Customer class that inherits the Person class. This class should add an attribute for
a customer number.
Create an Employee class that inherits the Person class. This class should add anattribute for
a PAN number.
The program should create a Customer or Employee object from the data entered bythe user,
and it should use this object to display the data to the user.
To do that, the program can use the isinstance() function to check whether an object is a
Customer or Employee object.
'''

#Program Source Code :
class Person:  # Creating parent class "Person"
    def __init__(self, fname="", lname="", email=""):  # creating parent class consructor
        self.fname = fname  # Assigning the values for fname,lname,email
        self.lname = lname
        self.email = email

    def getFullname(self):  # Method to get full name
        return self.fname+" "+self.lname  # returns fname+lane to the calling function

class Customer(Person):  # creating child class "Customer" that inherits parent class "Person"
    def __init__(self, fname, lname, email, cust_id):  # constructor for class "Customer"
        # calling constructor of parent class
        Person.__init__(self, fname, lname, email)
        # creating and assigning the value for new attribute "cust_id" for child classs "Customer"
        self.cust_id = cust_id

    def getCustId(self):  # creating method that returns "cust_id" to the calling function
        return self.cust_id

class Employee(Person):  # creating child class "Employee" that inherits parent class "Person"
    def __init__(self, fname, lname, email, PAN):  # constructor for child class "Employee"
        Person.__init__(self, fname, lname, email)
        self.PAN = PAN

    def getPAN_no(self):
        return self.PAN

def Display(obj):  # global method to display the details
    # checks if the object passed a "Customer" class object by using "isinstance()" function
    if isinstance(obj, Customer):
        print("Its a Customer class Object")
        print(f"Customer Name :: {obj.getFullname()}")
        print(f"Customer Number :: {obj.getCustId()}") 
    else:
        print("Its a Employee class Object")
        print(f"Employee Name :: {obj.getFullname()}")
        print(f"Employee PAN Number :: {obj.getPAN_no()}")

def main():  # main function to run the prog
    # creating object for "Customer" class and passing the values to constructor
    cust_obj = Customer("Lionel", "Messi", "lm@gmail.com", 1)       #20000 address
    # creating object for "Employee" class and passing the valus tpo the constructor
    emp_obj = Employee("Kylian", "Mbappe", "km@gmail.com", "No10")  #50000 address
    Display(cust_obj)
    print()
    Display(emp_obj)

if __name__ == "__main__":  # condition to check if there is a function named "main()" in the program
    main()  # class main function to run the program












    
