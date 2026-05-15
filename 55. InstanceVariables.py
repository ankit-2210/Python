# Instance variable:
# "Instance variables are the variables for which the value of the variable is different for every instance."
#
# We can also say that the value is different for every object that we create. Let us dive into some in-depth explanation. When we create a class, we define a few variables along with it. For example, we have created a class of Students, and we have defined a variable age.
# All the students cannot have the same age in a class, so we have assigned the variable an average age of 16.  Now, whenever we use an object to print the value of age, it will show 16. We can try to change the value of age, but it will create a new instance variable for the specific object that we are updating it for, hence defining the value to it.


# Class variable:
# "Class attributes are owned by the class directly, which means that they are not tied to any object or instance."
#
#  Same as in the above example, if we want to change the age for every instance from 16 to 17, then we can do it by using the class variable, which in this case is Student.
#
# The code for changing age using a class variable will be something like this:
# Students.age = 18


class Employee:
    no_of_leaves = 8
    pass


harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"


print(Employee.no_of_leaves)
print(Employee.__dict__)
Employee.no_of_leaves = 9  # Override it
print(Employee.__dict__)
print(Employee.no_of_leaves)
