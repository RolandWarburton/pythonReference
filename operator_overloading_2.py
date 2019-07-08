# operation overloading is taking operation signs and re-purposing them
# eg. making the * do something else


# turns the * into +
class Number:

    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        result = self.x + other.x
        return result


add1 = Number(3)
add2 = Number(4)
# takes the x attribute from add1 and add2
# takes the LHS (self.x) and adds it to the RHS (other.x) as defined by __mul__
print(add1 * add2)
