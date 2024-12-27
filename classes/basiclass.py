class car:
    def init(self):
        print(" i am class")

classobj = car()
classobj.init()

# class with init method with out arguments gives error so give self
# class person():
#     def __init__( ):
#         print("i am with init method with out self gives error")

# classobj = person()

class person():
    def __init__(self):
        print("i am with init method")

classobj = person()

class person():
    def _init_(my):
        print("i am with init method with own name argument")

classobj = person()