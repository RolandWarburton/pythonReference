# functions inside this class are called init functions
class Students:

    def __init__(self, name, id_number):
        # the purpose of this function is just to declare the variables for later
        # We can put data straight into the object straight away like this
        self.name = name
        self.id_number = id_number

    def set_data(self, a, b):
        self.name = a
        self.id_number = b

    def print_data(self):
        print("the name is {}. the contact is {}".format(self.name, self.id_number))


# create an object in the class
roland = Students("roland", 1)

# changing the data of the object
roland.set_data("owen", 2)

# print the data
roland.print_data()
