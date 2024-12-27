class Person():
    def __init__(self):
        self.name = ""
        self.age = 0
public = Person()
public.name = "somesh"
public.age = 51


# Protected
# A variable or method that is protected is only accessible from within the class itself, or one of its
# subclasses. _

class Person():
# Constructor
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def _speak(self):
        print(f"Hi. My name is {self.__name}.")
bob = Person("ss", 48)
print(bob._name)
bob._name = "rr"
print(bob._name)
# Output
# Bob
# Robert
# Notice that the variable _name is still accessible - you can read the value…and change it.


# Private
# A variable or method that is private is not accessible from outside of the class. Any attempt to do so
# will cause an error.
class Person():
# Constructor
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def __speak(self):
        print(f"Hi. My name is {self.__name}.")
    
    def __getname(self):
        return {self.__name}
        
bob = Person("Bob", 48)
print(bob.__getname())

#  to access the private variables use return key word