# Create a class named ‘Dog’. It should have a constructor which accepts its name,
# age and coat color. You must perform the following operations:

#  a. It should have a function ‘description()’ which prints the name and age of the dog.
#  b. It should have a function ‘get_info()’ which prints the coat color of the dog.
#  c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’.
#  It should have at least two methods of its own.
#  d. Create objects and implement the above functionalities.

class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"The name of the dog is {self.name}")
        print(f"The dog's age is {self.age}")

    def get_info(self):
        print(f"The coat color of {self.name} is {self.coat_color}")

class JackRussellTerrier(Dog):

    def weight(self, weight=16):
        self.weight = weight
        print(f"The weight of {self.name} is {self.weight} pounds")

    def life_span(self, lifespan = 15):
        self.lifespan = lifespan
        print(f"The lifespan of {self.name} is {self.lifespan} years")

class Bulldog(Dog):

    def __init__(self, name, age, coat_color="White",gender="Female"):
        super().__init__(name, age, coat_color)
        self.gender = gender

    def height(self, height=16):
        self.height = height
        print(f"The height of {self.name} is {self.height} inches")

    def bark(self, bark):
        self.bark = bark
        print(f"{self.name} is a {self.gender} and says {self.bark}")


snoopy = JackRussellTerrier("Snoopy", 4, "White")
snoopy.description()
snoopy.get_info()
snoopy.weight(9)
snoopy.life_span()

print("-------------------------")

tom = JackRussellTerrier("Tommy", 9, "Brown")
tom.description()
tom.get_info()
tom.weight()
tom.life_span(18)

print("-------------------------")

bullyboo = Bulldog("Bully Boo", 18)
bullyboo.description()
bullyboo.get_info()
bullyboo.height(14)
bullyboo.bark("Woooofffyyyy!")

print("-------------------------")

rocky = Bulldog("Rocky", 7, "Yellow", "Male")
rocky.description()
rocky.get_info()
rocky.height(17)
rocky.bark("Woooofffyyyy Wooffy Wooo!")

