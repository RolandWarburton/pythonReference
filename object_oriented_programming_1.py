# functions inside this class are called init functions
class Students:

    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def get_data(self, a, b):
        self.name = a
        self.id_number = b

    def put_data(self):
        print("the name is {}. the contact is {}".format(self.name, self.id_number))


# inherits stuff from the Students class
class ScienceStudent(Students):
    def __init__(self, age):
        self.age = age

    def science(self):
        print("i am a science student that's {} years old".format(self.age))


# you need to pass some stuff in to begin with. so roland is arbitrary right now until its passed in
roland = Students("NULL", 0)
roland.get_data("roland", 1)
roland.put_data()

rob = ScienceStudent(20)
rob.science()
rob.get_data("rob", 2)
rob.put_data()
