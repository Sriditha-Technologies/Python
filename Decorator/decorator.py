def function1(function):
    def wrapper():
        print('hello')
        function()
        print("welcome to python tutorial")
    return Wrapper
    def function2():
        print("amul")
function2=function1(function2)
function2()