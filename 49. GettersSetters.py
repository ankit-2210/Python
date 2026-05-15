# Getters in Python are methods that are used to access the values of an object's properties.
# They are used to return the value of a specific property, and are typically defined using
# the @property decorator. Here is an example of a simple class with a getter method:


class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def ten_value(self):
        return 10 * self._value

    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value / 10


obj = MyClass(10)
obj.ten_value = 200
print(obj.ten_value)
obj.show()


# Setters
# It is important to note that the getters do not take any parameters and we
# cannot set the value through getter method.For that we need setter method
# which can be added by decorating method with @property_name.setter


class MyClass1:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


obj1 = MyClass1(11)
obj1.value = 20
print(obj1.value)
