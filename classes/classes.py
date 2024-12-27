# class
# object
# encapsulation
# inheritance
# polymorphism
# abstraction

class Person:
# Constructor
    def __init__(self, name , designation):
        self.name = name
        # self._designation = designation # protected
        self.designation = designation 
    
    def designationn(self):
        print(f"Hi. My name is {self.name}.  i am a {self.designation}")
        
# person_one = Person("somesh")
# person_one.designationn()
# person_two = Person("snh")
# person_two.designationn()

#inheritance

class student(Person):
    def __init__(self, age):
        super().__init__(self, designation="student")
        self.age = age
    def designationn(self):
        print(f"Hi. My name is {self.name}.  i am a {self.designation}")
    
   

student_obj = student(30)


student_obj.name ="somesh"

student_obj.designation ="new"

student_obj.designationn()


class tshirt():
    def __init__(self, type):
        #self.__type = type # private
        self._type = type # private not accesble outside class for only with in that class
        
    def shirttype(self):
        print(f" shirt type is {self.type}")

shirt_type = tshirt("t shirt")

#print(shirt_type.__type)   # error     
        








        
