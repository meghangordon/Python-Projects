#Create a class that uses encapsulation. Requirements include:


#This class should make use of a private attribute or function.

#This class should make use of a protected attribute or function.

#Create an object that makes use of protected and private.

#Add comments throughout your Python explaining your code.

#Upload your code to GitHub and submit your link below.



## Protected class - cat
class Cat:
    def __init__(self):
        self.__protectedCat = ''
        
obj = Cat()
obj._protectedCat = 'Meow'
print(obj._protectedCat)

##Private class - Dog
class Dog:
    def __init__(self):
        self.__privateDog = ''
        
    def getPrivateDog(self):
        print(self.__privateDog)

    def setPrivateDog(self, private):
        self.__privateDog = private

obj2 = Dog()
obj2.getPrivateDog()
obj2.setPrivateDog('Bork')
obj2.getPrivateDog()


