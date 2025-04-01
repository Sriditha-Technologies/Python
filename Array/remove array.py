import array as arr
a=arr.array('d',[1.1,2.2,3.8,3.1,3.7])
print("popping last element",a.pop(1))
print("popping 4th element",a.pop(3))
a.remove(1.1)
print(a)