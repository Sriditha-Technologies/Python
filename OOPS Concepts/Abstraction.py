for abc import ABC, abstractmethod
class car(ABC):
    @abstractmethod
    def price_inc(self):
        pass

class supercar(car):
    def __init__(self,modelname,yearn,price,cc):
        super. __init__(modelname,yearn,price)
        self.cc=cc
 
    def price_inc(self):
        self.price=int(self.price*2)

honda=supercar('city',2017,1000000)
tata=car('Bolt',2016,600000)

honda.cc=1500
honda.price_inc()
print(honda.price)
