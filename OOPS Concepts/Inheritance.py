class car():
    def __init__(self,modelname,yearn,price):
        self.modelname=modelname
        self.yearn=yearn
        self.price=price
    
    def price_inc(self):
        self.price=int(self.price*1.15)

class supercar(car):
    def __init__(self,modelname,yearn,price,cc):
        super. __init__(modelname,yearn,price)
        self.cc=cc
    
honda=supercar('city',2017,1000000)
tata=car('Bolt',2016,600000)
honda.cc=1500
honda.price_inc()
print(honda.price)
    
    