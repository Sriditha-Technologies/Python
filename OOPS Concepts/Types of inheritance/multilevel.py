class parent:
    def func1(self):
        print("this is function 1")

class parent2(parent):
    def func3(self):
        print("this is function 3")

class child(parent2):
    def func2(self):
        print("this is function 2")

ob=child()
ob.func1()
ob.func3()
