class Myclass:
    __hidden = 0

    def add(self, a):
        self.__hidden += a
        print(self.__hidden)


object1 = Myclass()
object1.add(5)

# try to access 'hidden'
print(object1.__hidden)