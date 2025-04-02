class car():
    def __init__(self,modelname,yearn,price):
        self.modelname=modelname
        self.yearn=yearn
        self.price=price

honda =car('city',2017,1000000)
tata=car('Bolt',2016,600000)

honda.cc=1500
print(honda.__dict__)