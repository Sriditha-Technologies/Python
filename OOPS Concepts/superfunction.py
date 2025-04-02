class parent:
    def func1(self):
        print("this is fuinction 1")

class child(parent):
    def func2(self):
        super().func1()
        print("this is function2")

ob=child()
ob.func2()