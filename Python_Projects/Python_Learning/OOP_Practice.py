class Vehicle: # Syntax to create a class
    Amount_of_Cars_Created = 0 # This is called a class variable, which is shared among all instances of the class

    def __init__(self, Name: str, Wheels: int, Color: str, Price: float, Max_Speed: float): # When defining __init__, ALWAYS pass self as the first variable
        # __init__ is not required though, it means for initiate and will ALWAYS run when the class is created
        
        self.Name = Name # This is called a instance variable, which are unique to different classes (Passing in different arguments will create different instance variables)
        self.Wheels = Wheels
        self.Color = Color
        self.Price = Price
        self.Max_Speed = Max_Speed
        Vehicle.Amount_of_Cars_Created += 1
        # self refers to the current object, for example, the self keyword right now is refering to the class Vehicle, it creates new attributes or variables to the class
        # For example, self.Name creates a new variable called Name inside of Vehicle and can be referred to as Vehicle.Name

    def Display_Vehicle_Attributes(self) -> None: # You can also create methods (functions) inside of classes, ALWAYS pass self as the first variable
        print(f''''
              
            Name: {self.Name}
            Wheels: {self.Wheels}
            Color: {self.Color}
            Price: {self.Price}
            Max Speed = {self.Max_Speed}

              ''')


This_Vehicle = Vehicle("Apollo", 4, "Bright Red", 100000.0, 100.0) # In case you have an __init__ method inside of your class, create the class and pass in the corresponding arguments accordingly
Another_Vehicle = Vehicle("Yeetus", 4, "Dark Blue", 75000.0, 80.0)

print(f"Total Amount of Cars Created: {Vehicle.Amount_of_Cars_Created}")

This_Vehicle.Age = 15 # You can also add new attributes to a class after it has been created
print(f"The Vehicle Apollo is {This_Vehicle.Age} years old.") # Pylance puts a squiggly line under Age because it doesn't see Age as an attribute of Vehicle since it was added after the class was created (Strict Mode)

class Calculator:
    def Calculate_Result(self, Number1: float, Number2: float, Operation: str) -> float:
        if Operation == "+":
            return Number1 + Number2
        elif Operation == "-":
            return Number1 - Number2
        elif Operation == "*":
            return Number1 * Number2
        elif Operation == "/":
            return Number1 / Number2
        else:
            print("Invalid Operation")
            return 0.0 # Return 0.0 to avoid returning None and causing errors in the program

This_Calculator = Calculator()

The_Result = This_Calculator.Calculate_Result(100, 20, "/")
print(f"The Result is: {The_Result}")
print(f"The remainder is {float(100 % 20)}")

class Human():
    def __init__(self, First_Name: str, Last_Name: str, Age: int):
        self.Name = f"{First_Name} {Last_Name}"
        self.Age = Age
    
    def Display_Human_Info(self) -> None:
        print(f''''
              
            Name: {self.Name}
            Age: {self.Age}

              ''')
        
    def Celebrate_Birthday(self) -> None:
        self.Age += 1
        print(f"Happy Birthday {self.Name}! You are now {self.Age} years old.")

    def __str__(self) -> str: # The __str__ method is just a string when you want to print the class object itself
        return "The Human Class!" # This will be printed when you print the class object itself
    
class Student(Human): # This is called inheritence, which allows the child class to inherit attributes and methods from the parent (inherited) class
    def __init__(self, First_Name: str, Last_Name: str, Age: int, Student_ID: int, Grade_Level: int): # Defining a new __init__ method in the child class

        super().__init__(First_Name, Last_Name, Age) # When defining a new __init__ method in the child class, you need to use to super() function with the parent's __init__ method's parameters to inherit the parent's attributes
        # Syntax: super().__init__(Parent_Class_Parameters)
        # This will make the child class override the parent's __init__ method but still inherit the parent's attributes
        # Make sure you pass in all of the parent's __init__ method parameters when using super() or it'll break unless you have default parameters in the parent's __init__ method

        self.Student_ID = Student_ID
        self.Grade_Level = Grade_Level
        # All you have to do last is just define the new attributes that are unique to the child class

    # def __init__(self, First_Name: str, Last_Name: str, Age: int):
    #     Human.__init__(self, First_Name, Last_Name, Age)
    # However, if you want to keep the parent's __init__ method without overriding it, you can just call the parent's __init__ method directly by defining the new __init__ and then calling the parent's __init__ method with the class name
    # Or just don't define a new __init__ method in the child class at all

    def __str__(self) -> str:
        return "The Student Class!"
    
    def Calculate_GPA(self, Grades: list[int]) -> float:
        if len(Grades) == 0:
            return 0.0
        return sum(Grades) / len(Grades)
    
    def Display_Student_Info(self) -> None:
        print(f''''
              
            Name: {self.Name}
            Age: {self.Age}
            Student ID: {self.Student_ID}
            Grade Level: {self.Grade_Level}

              ''')
    

Dylan = Student("Dylan", "Zhang", 15, 2940206, 10)
Dylan.Display_Student_Info()
Dylan.Celebrate_Birthday()
print(f"Dylan's Age: {Dylan.Age}")
print(Dylan)

My_Grades = [4, 4, 4, 3, 4, 3, 4, 4]
GPA = Dylan.Calculate_GPA(My_Grades)
print(f"Dylan's GPA is: {GPA}")

class Plane:
    def __init__(self, Name: str):
        self.Name = Name

    def Move(self) -> None:
        print("Whoosh Whoosh!")

class Boat:
    def __init__(self, Name: str):
        self.Name = Name

    def Move(self) -> None:
        print("Splish Splash!")

class Car:
    def __init__(self, Name: str):
        self.Name = Name

    def Move(self) -> None:
        print("Vroom Vroom!")

Car1 = Car("idk")
Boat1 = Boat("yeet")
Plane1 = Plane("skrrt")

for x in (Car1, Boat1, Plane1): # I used this example in w3schools. This is called polymorphism, which allows you to call the same method / functions on different classes
    print(x.Name)
    x.Move()

class Animal:
    def __init__(self, Name: str):
        self.Name = Name
        self.Is_Alive = True
    
    def Eat(self) -> None:
        print(f"{self.Name} is eating.")

    def Sleep(self) -> None:
        print(f"{self.Name} is sleeping. Night Night!")

class Prey(Animal):
    def Flee(self) -> None:
        print(f"{self.Name} is fleeing!")

class Predator(Animal):
    def Hunt(self) -> None:
        print(f"{self.Name} is hunting!")

class Carnivore(Prey, Predator): # Example of both Multilevel and Multiple Inheritence as it inherits from both Prey and Predator (Multiple) and Prey and Predator both inherit from Animal (Multilevel)
# Basically Multiple is <Class_Name>(Parent1, Parent2) and Multilevel is <Class_Name>(Parent) where Parent also inherits from another class
    pass

class Dog(Animal): # More inheritence practice with Animals to Dogs
    def Bark(self) -> None:
        print(f"{self.Name} is barking. Woof Woof!")

Dog1 = Dog("Buddy")
Dog1.Bark()
Dog1.Eat()
Dog1.Sleep()

Rabbit = Prey("Rabbit lol")
Lion = Predator("This Lion")
Fish = Carnivore("Fishy")

Lion.Hunt()
Rabbit.Flee()
Fish.Hunt()
Fish.Flee()

class User():
    def __init__(self, Username: str, Email: str, Password: str, Phone_Number: str):
        self.Username = Username
        self._Email = Email # This is a protected variable, it signifies that it should not be accessed outside of the class or its subclasses (One Underscore)
        self.__Password = Password # This is a private variable, this is also called name mangling, and Python strictly enforces that this variable cannot be accessed outside of the class (Two Underscores)
        self._Phone_Number = Phone_Number

    def Get_Password(self) -> str: # A function to retrieve the private variable __Password
        return self.__Password
    
    # This is an example of encapsulation, which means restricting direct access to class variables and only being accessible internally through the class methods and functions
    
    def Get_Email(self) -> str:
        return self._Email
    
    def Get_Phone_Number(self) -> str:  
        return self._Phone_Number
    
    def Set_Password(self, New_Password: str) -> None: # A function to set a new value to the private variable __Password
        self.__Password = New_Password
    
    def Set_Email(self, New_Email: str) -> None:
        self._Email = New_Email
    
    def Set_Phone_Number(self, New_Phone_Number: str) -> None:
        self._Phone_Number = New_Phone_Number

John_Doe = User("John_Doe", "JohnDoe@gmail.com", "SuperDuperSecretPassword123!", "123-456-7890")

print(John_Doe._Email) # This will work, however, it is NOT recommended to access protected variables outside of the class. Even python will give you a warning for this.
# print(John_Doe.__Password) # This will not work because __Password is a PRIVATE variable and cannot be accessed outside of the class. Python will throw an AttributeError.
print(John_Doe.Get_Password()) # Use the Getter method Get_Password() to access the private variable __Password instead since it is a private property. This is also called encapsulation since the variable is being accessed through a class method.

print(John_Doe._User__Password) # This is name mangling, which allows access to private variables outside of the class by using ._ClassName__VariableName. This is NOT recommended and getters and setters should be used instead.
# (Also why you trying to access private members outside of the class? Use getters and setters! Private members are private to restrict access from outside the class!)

John_Doe.Set_Password("NewSecretPasswordidkbro") # Use the Setter method, in this case, Set_Password() to set the new value for the private variable __Password
print(John_Doe.Get_Password()) # Use the Getter method to verify that the Setter method worked

class Dog_Owner:
    def __init__(self, Name: str, Address: str, Phone_Number: str):
        self.Name = Name
        self.Address = Address
        self.Phone_Number = Phone_Number

class Doggy:
    def __init__(self, Name: str, Breed: str, Age: int, Owner: Dog_Owner): # Owner's type is Dog_Owner class, which accepts a class instance that is of type Dog_Owner
        self.Name = Name
        self.Breed = Breed
        self.Age = Age
        self.Owner = Owner

    def Bark(self) -> None:
        print(f"{self.Name} says Woof Woof!")

Owner1 = Dog_Owner("Alice", "123 Main St", "555-1234")
Dog1 = Doggy("Buddy", "Golden Retriever", 3, Owner1)
# Dog2 = Doggy("Max", "Beagle", 5, Dog1) # Here this will error because Dog1 is not of type Dog_Owner, it is of type Doggy

class Company_A:
    def __init__(self, Name: str):
        self.Name = Name

    class Employee: # These are examples of a nested or inner class, which is a class defined inside of another class
        def __init__(self, First_Name: str, Last_Name: str, Position: str):
            self.Name = f"{First_Name} {Last_Name}"
            self.Position = Position

        def Work(self) -> None:
            print(f"Beep Boop! {self.Name} is working as a {self.Position} at Company A.")

class Company_B:
    def __init__(self, Name: str):
        self.Name = Name

    class Employee:
        def __init__(self, First_Name: str, Last_Name: str, Position: str):
            self.Name = f"{First_Name} {Last_Name}"
            self.Position = Position

        def Work(self) -> None:
            print(f"Woooh! I'm making a lot of food tonight! {self.Name} is working as a {self.Position} at Company B.")

Employee1 = Company_A.Employee("Bob", "Smith", "Engineer")
Employee2 = Company_B.Employee("Charlie", "Brown", "Chef")

from abc import ABC, abstractmethod # ABC - Abstract Base Class

class Another_Vehicle_Class(ABC): # I changed it to Another_Vehicle_Class to avoid name conflict with previous Vehicle class

    @abstractmethod # Abstract Method are methods that are declared, but contain no implementation and must be implemented by any subclass
    def Move(self) -> None:
        pass

    @abstractmethod
    def Stop(self) -> None:
        pass

class Another_Car(Another_Vehicle_Class): # I changied it from Car to Another_Car to avoid name conflict with previous Car class

    # The subclasses that inherit from the abstract class must implement all abstract methods defined in the abstract class or else Python will throw an error
    def Move(self) -> None:
        print("Vroom Vroom! Car is moving!")

    def Stop(self) -> None: # Let's just say I didn't define Stop, then Python will throw a TypeError when I try to instantiate the car Class because it didn't implmement all abstract methods from Vehicle
        print("Car is stopping!")

# This_Random_Vehicle = Vehicle() # Python will throw a TypeError because you cannot instantiate an abstract class directly
This_Car = Another_Car() # This will work because Car is a concrete class that implements all abstract methods from the abstract class Vehicle
This_Car.Move()
This_Car.Stop()

# Duck typing: "If it looks like a duck and quacks like a duck, it's a duck"
# Basically, if an object resembles another then it can be considered the same type even if it doesn't inherit from the same class

class Another_Animal():
    Alive = True

class Another_Dog():
    def Speak(self) -> None:
        print("Woof Woof!")

class Another_Cat():
    def Speak(self) -> None:
        print("Meow Meow!")

class Another_Second_Car():
    def Speak(self) -> None:
        print("Honk Honk!")

The_Animals: list[object] = [Another_Dog(), Another_Cat(), Another_Second_Car()]

for animal in The_Animals:
    animal.Speak() # Even though the Car class is not an animal, it has the Speak() method which considers it an animal due to duck typing
    # This is another way to achieve polymorphism - Duck Typing
    # Oh yeah, Python put a red swiggly line here because the type of the method is unknown

# Aggregation is an assocation between two classes and they both have a "has-a" relationship with each other and can exist independently without each other

class Electronic_Store:
    Devices: list[Device] = [] # Created an empty list for specifically the class type of Device, meaning Python will know that it should contains instances that belong to the class Device and not anything else.

    def Add_Device(self, Electronic: Device) -> None:
        self.Devices.append(Electronic) # Now add that Device class into the list Devices
        # This is called aggregation. The class Electronic Store holds class instances of Device forming a "has-a" relationship and both classes can exist independently.

    def Display_Products(self) -> None:
        
        for device in self.Devices:
            
            print(f"""

    Device: {device.Device_Name}
    Model: {device.Model}
    Price: {device.Price}
    Unique ID: {device.Unique_Store_ID}

        """)

class Device:
    def __init__(self, Device_Name: str, Model: str, Price: float, Unique_Store_ID: int):
        self.Device_Name = Device_Name
        self.Model = Model
        self.Price = Price
        self.Unique_Store_ID = Unique_Store_ID

    def __str__(self) -> str:
        return self.Device_Name
    
    def Purchase_Device(self, Store: Electronic_Store) -> None:
        Store.Devices.remove(self)

Nearby_Electronic_Store = Electronic_Store()

Mobile_Phone = Device("Iphone 17", "Base", 999.99, 1)
Gaming_Desktop = Device("Gaming Computer", "ASUS", 1500.0, 2)
Console = Device("PS5", "PlayStation", 499.99, 3)

Nearby_Electronic_Store.Add_Device(Mobile_Phone)
Nearby_Electronic_Store.Add_Device(Gaming_Desktop)
Nearby_Electronic_Store.Add_Device(Console)

Nearby_Electronic_Store.Display_Products()

Gaming_Desktop.Purchase_Device(Nearby_Electronic_Store)
Nearby_Electronic_Store.Display_Products()

# Composition is the association between two classes with a "owns-a" relationship. Basically another class "owns" another class and that owned class CANNOT exist without the owner class

class Master_Bedroom:
    def __init__(self, Color: str, Size: float):
        self.Color = Color
        self.Size = Size

class House:
    def __init__(self, Owner: str, Main_Bedroom: Master_Bedroom):
        self.Rooms: list[Master_Bedroom] = []
        self.Owner = Owner
        self.Rooms.append(Main_Bedroom)

    def __str__(self) -> str:
        return "Nice, comfortable home!"

    def Demolish(self) -> None:
        del self

My_House = House("Dylan", Master_Bedroom("Blue", 250.0))
print(My_House)

import math # Math library in Python

class This_Circle:
    def __init__(self, color: str, is_filled: bool, radius: float):
        self.color = color
        self.Is_Filled = is_filled
        self.Radius = radius

    def __str__(self) -> str:
        return f"A circle that is {self.color} and {"is filled" if self.Is_Filled else "not filled"}" # Termary operator (if-else statement) Inline operation
    
    def Calculate_Area(self) -> float:
        return math.pi * (math.pow(self.Radius, 2))
    
Circle_Thingy = This_Circle("Light Blue", True, 30)
print(Circle_Thingy)
print(Circle_Thingy.Calculate_Area())

class Rectangle:
    def __init__(self, length: float, width: float):
        self.__length = length
        self.__width = width

    @property # This is the property decorater, which gives extra functionality to an attribute in the class
    def length(self) -> float:
        return round(self.__length, 1)
    
    @property
    def width(self) -> float:
        return round(self.__width, 1)
    
    def Calculate_Area(self) -> float:
        return self.length * self.width
    
    def __str__(self):
        return "Yeah, I'm a literal rectangle!"
    
A_Literal_Rectangle = Rectangle(5, 4)
print(A_Literal_Rectangle)
print(A_Literal_Rectangle.Calculate_Area())

class Pupil: # Renamed to Pupil because student is already taken
    Amount_of_Students: int = 0
    Total_GPA: float = 0.0

    def __init__(self, Name: str, GPA: float):
        self.Name = Name
        self.GPA = GPA

        Pupil.Amount_of_Students += 1
        Pupil.Total_GPA += GPA

    def __str__(self) -> str:
        return f"{self.Name} has a GPA of {self.GPA}"

    @classmethod
    def Get_Amount_of_Students(cls) -> str: # Class methods take cls (class) as the first parameter instead of self, which can only access the class attributes and not class instances properties and they can also be accessed and called directly from the class itself
        return f"This class has {cls.Amount_of_Students} students!"
    
    @classmethod
    def Calculate_Average_Class_GPA(cls) -> float:
        if cls.Amount_of_Students == 0 or cls.Total_GPA == 0.0:
            print("Cannot calculate total GPA!")
            return 0.0
        else:
            return cls.Total_GPA / cls.Amount_of_Students
        
Anthony = Pupil("Anthony", 3.5)
Alexander = Pupil("Alexander The Great", 4.0)
Christian = Pupil("Christian", 3.0)

for Pupil_class in Anthony, Alexander, Christian:
    print(Pupil_class)

print(Pupil.Get_Amount_of_Students())
print(f"The class average GPA is {Pupil.Calculate_Average_Class_GPA()}")