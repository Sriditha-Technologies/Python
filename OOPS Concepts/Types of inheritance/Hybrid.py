class parent:
    def func1(self):
        print("this is function 1")

class parent2(parent):
    def func3(self):
        print("this is function 3")

class parent3(parent):
    def func4(self):
        print("this is function 4")


class child(parent,parent3):
    def func2(self):
        print("this is function 2")

ob=child()
ob.func1()
ob.func4()
