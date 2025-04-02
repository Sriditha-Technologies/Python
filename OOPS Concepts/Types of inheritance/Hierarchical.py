class parent:
    def func1(self):
        print("this is function 1")

class parent2(parent):
    def func3(self):
        print("this is function 3")

class child(parent):
    def func2(self):
        print("this is function 2")

ob=child()
ob1.parent2()
ob.func1()
ob1.func1()
