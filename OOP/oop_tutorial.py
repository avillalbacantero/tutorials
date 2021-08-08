from __future__ import annotations

# Let's define a custom class
class Animal(object):  # every class is a child of the object class
    # class Animal: # this is valid as well

    # First we need the constructor method
    # The first argument is always a 'self'.
    def __init__(self, name: str, age: int, owner: str) -> None:
        # Everytime we create a new instance of the class, this method
        # will be executed

        # Here we are giving values to the attributes, which are
        # variables associated to the object.
        # Self is a reference to the object instance but inside the
        # class.
        self.name = name
        self.age = age
        self.owner = owner

    # Now we are going to define some methods, which are like functions
    # but they are associated with an object as well
    def say_hello(self) -> None:
        print(f"Hi! My name is {self.name}!")

    # Let's overload a simple dunder method. These can be used to
    # override functionality for built-in functions for custom classes.
    def __str__(self) -> str:
        # For example, this method returns a nice string representation
        # of the class.
        return f"Name: {self.name} - Age: {self.age} " f"- Owner: {self.owner}"

    # We can overload complex methods as well. For example, let's say
    # that for us adding two animal means they have a child
    def __add__(self, other_animal: Animal) -> Animal:
        return Animal(
            f"The child of {self.name} and {other_animal.name}",
            0,
            f"{self.owner} and {other_animal.owner}",
        )

    # Let's overload some more methods. These are for comparing animals,
    # which means comparing animals' ages for us.
    def __gt__(self, other_animal: Animal) -> bool:
        return self.age > other_animal.age

    def __ge__(self, other_animal: Animal) -> bool:
        return self.age >= other_animal.age

    def __lt__(self, other_animal: Animal) -> bool:
        return self.age < other_animal.age

    def __le__(self, other_animal: Animal) -> bool:
        return self.age <= other_animal.age

    def __eq__(self, other_animal: Animal) -> bool:
        return self.age == other_animal.age


# Let's do class inheritance. We create a child class called Dog from
# the parent class called Animal. All methods and attributes from Animal
# can be used by any Dog object.
class Dog(Animal):

    # Here we are going to define some class attributes. These attributes
    # belong to the class, not to the object instance, but they are shared
    # across all the class instances.
    SOUND = "Bark!"  # for example, the sound of a Dog is 'Bark!'
    all_dogs = []  # we can have lists of the created instances too

    # Now we are creating the constructor. To do this, we have to call
    # the parent class constructor
    def __init__(
        self, name: str, age: int, owner: str, pedigree: bool
    ) -> None:
        # We call the parent class (known as superclass) constructor
        # super() is a reference to the parent class.
        super().__init__(name, age, owner)
        # We can have attributes which are specific to the child class
        # as well
        self.pedigree = pedigree
        # And we can override attributes from the parent class too
        self.owner = f"{owner} / Dog Owner"

        # As a new instance has been created, we append it to the list
        Dog.all_dogs.append(self)
        # self.all_dogs.append(self)  # this is valid too

    # Now, we are going to write a custom method for the child class
    def speak(self) -> None:
        print(Dog.SOUND)
        # print(self.SOUND)  # we can do it like this too

    # We can also override a method from the parent class
    def say_hello(self) -> None:
        print(f"Hi! My name is {self.name} and I'm a dog! :)")

    def __str__(self) -> str:
        return f"{super().__str__()} - Pedigree: {self.pedigree}"

    def __add__(self, other_dog: Dog) -> Dog:
        return Dog(
            f"The child of {self.name} and {other_dog.name}",
            0,
            f"{self.owner} and {other_dog.owner}",
            self.pedigree and other_dog.pedigree,
        )

    # Let's write now a static method. This is a function that does not
    # depend neither on the class nor the object instance but it's useful
    # to have it inside the class to mantain a good code organization.
    @staticmethod  # we use this decorator to define a static method
    def speak_some_times(n_times: int) -> None:  # here we don't pass 'self'
        # So we cannot use 'self' inside this function. See the speak()
        # method as well: actually, we are not using any object
        # attribute nor method; that indicates it could be static too.
        for _ in range(n_times):
            print(Dog.SOUND)

    # Now, let's create a class method. This method is referred to the
    # class itself, not to any instance.
    @classmethod  # we use this decorator to define a class method
    def num_dogs(cls) -> int:  # we pass 'cls' as parameter
        # 'cls' is a reference to the class itself
        return len(cls.all_dogs)


# Let's do the same with a Cat
class Cat(Animal):

    SOUND = "Meow!"
    all_cats = []

    def __init__(self, name: str, age: int, owner: str) -> None:
        super().__init__(name, age, owner)
        self.owner = f"{owner} / Cat Owner"
        Cat.all_cats.append(self)

    # Now, we are going to write a custom method for the child class
    def speak(self) -> None:
        print(Cat.SOUND)

    # We can also ovewride a method from the parent class
    def say_hello(self) -> None:
        print(f"Hi! My name is {self.name} and I'm a cat! :)")

    @staticmethod
    def speak_some_times(n_times: int) -> None:
        for _ in range(n_times):
            print(Cat.SOUND)

    @classmethod
    def num_cats(cls) -> int:
        return len(cls.all_cats)


# Animal, Dog and Cat and not-private classes. Let's say that for some
# reason we want to create a private class.
# Private classes are only accesible from the same file but not from
# everywhere. We use the underscore '_' to mark that a class is private.
# However, this doesn't have any real functionality, it's just a way
# to communicate to other devs that out intention was to create a private
# class
class _PrivateClass(object):
    pass


# Let's create another class but this time it will be not private, as with
# Animal Dog and Cat. Public classes can be accessed from anywhere.
class NotPrivateClass(object):

    # Let's declare a public method for this class
    def foo(self) -> None:
        print("Hi!")

    # And now let's declare a private method for this class
    def _private_foo(self) -> None:
        print("I'm privated, sorry.")


if __name__ == "__main__":

    # Let's take a look about how objects are created in Python:
    x = 5  # this is an object
    y = "This is an object as well"
    # x is an instance of the class int
    print(type(x))
    # y is an instance of the class str as well
    print(type(y))
    # Each class has its own methods
    print(y.upper())
    # And this command can help you to visualize those methods
    print(help(str))

    # We can use custom classes in the same way.
    # Let's create an instance of the object Animal
    # Here we are creating an Animal object with some attributes
    sira = Animal("Sira", 6, "Cristina")
    sira.say_hello()
    print(sira.name)  # we can access the object attributes like that

    # Another one
    casper = Animal("Casper", 5, "Ana")
    casper.say_hello()

    # Ok, now let's do them speak
    # However, one animal is a dog and one animal is a cat, so they'll
    # speak differently. We use class inheritance for that.
    sira = Dog("Sira", 6, "Cristina", True)
    sira.say_hello()
    sira.speak()

    casper = Cat("Casper", 5, "Ana")
    casper.say_hello()
    casper.speak()

    # Now let's see the nicely string representation of each of them
    # We can call it by doing:
    print(sira.__str__())
    # Or by doing:
    print(str(sira))  # which is more elegant
    # If we would not have overloaded a new __str__ method for Dog, the
    # output would have been: <__main__.Dog object at 0x000001AA7E224160>
    # This works for the Cat as well, since the parent class Animal has
    # an overrided __str__ method
    print(str(casper))

    # Let's say now Sira meets another dog and they have a puppy
    rex = Dog("Rex", 6, "Ana", True)
    rex.say_hello()
    puppy = sira + rex  # this calls the __add__ method
    puppy.say_hello()
    puppy.speak()
    print(type(puppy))  # the puppy is a Dog as well
    print(f"Puppy pedigree: {puppy.pedigree}")  # and it's pedigree

    # We can compare the animals ages as well
    print(rex > casper)  # this calls the __gt__ method
    print(casper >= sira)  # __ge__ method
    print(rex == sira)  # __eq__ method

    # Let's now use one static method of the class Dog. We don't need
    # any Dog instance to do it.
    Dog.speak_some_times(3)
    # However, we can also make sira or rex speak some times
    sira.speak_some_times(3)
    rex.speak_some_times(3)
    Cat.speak_some_times(1)  # some cat is listening and replying...

    # Let's now use the class method from the Dog class to know how many
    # dogs we currently have
    print(f"There are: {Dog.num_dogs()} dogs right now.")
    # And how many cats
    print(f"There are: {Cat.num_cats()} cats right now.")

    # Finally, let's look at public and private classes.
    # You can create an instance of a private class:
    private = _PrivateClass()
    # And call private methods as well
    public = NotPrivateClass()
    public.foo()
    public._private_foo()
