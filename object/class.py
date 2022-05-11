from curses import ACS_GEQUAL


def example_class():
    # Create a class named MyClass, with a property named x.
    class MyClass:
        x = 5
    
    # Use class Myclass to create objects.
    p1 = MyClass()
    print(p1.x)

    # All classes have a function called __init__(), which is always executed
    # when the class is being initiated. 
    # Use the __init__() function to assign values to object properties, 
    # or other operations that are necessary to do when the object is being created:

    # Create a class named Person, use the __init__() function
    # to assign values for name and age:
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    p1 = Person("John", 36)

    print(p1.name)
    print(p1.age)
    # print(p1), print(Person) or print(p1.name, age)
    # -> Error, not allowed

    # Object Methods
    # Methods in objects are functions that belong to the object.
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.name = age

        def myfunc(self):
            print("Hello my name is " + self.name)
    
    p1 = Person("John", 36)
    p1.myfunc()

    # Self parameter 
    # The self parameter is a reference to the current instance of the class, 
    # and is used to access variables the belongs to the class.
    # It does not have to be named self, you can call it whatever you like, 
    # but it has to be the first parameter of any function in the class:
    class Person:
        def __init__(mysillyobject, name, age):
            mysillyobject.name = name
            mysillyobject.age = age

        def myfunc(abc):
            print("Hello my name is " + abc.name)

    p1 = Person("John", 36)
    p1.myfunc()

    # Modify object properties
    p1.age = 40

    # Delete object properties
    def p1.age 

    # Delete objects
    del p1

    # The pass statement
    # class definitions cannot be empty, but if you for some reason have a
    # class definition with no content, put in the pass statement to avoid 
    # getting an error.

    class Person:
        pass

    











