def function1(function):
    def wrapper(*args,**kwargs):
        print("hello")
        function(*args,**kwargs)
        print("welcome to python tutorial")
    return wrapper
    @function1
    def function2(name):
        print(f"{name}")
        function2("amul")