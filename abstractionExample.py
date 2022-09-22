
#Your class should contain at least one abstract method and one regular method.  

#Create a child class that defines the implementation of its parents abstract method.

#Create an object that utilizes both the parent and child methods.
 
#Add comments throughout your Python explaining your code.



from abc import ABC, abstractmethod ##parent class and abstract method
class HOA(ABC):
    def payDues(self, amount):
        print("Your monthly HOA fees total bill: ",amount)

    @abstractmethod
    def payment(self, amount):
        pass
##childclass
class DebitCardPayment(HOA):
    def payment(self, amount):
        print('Your overpayment amount of {} exceeded your $240 monthly dues limit, \
              please only pay for one month at a time.  '.format(amount))

obj = DebitCardPayment()
obj.payDues("$240")
obj.payment("$480")
    
