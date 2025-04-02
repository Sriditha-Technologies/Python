class parent:
    def func1(self):
        print("this is function 1")
class child(parent):
    def func2(self):
        print("this is function 2")

ob=child()
ob.func1()
