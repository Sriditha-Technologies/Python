import time
a=time.localtime()
b=time.mktime(a)
print(b)
c=time.asctime(a)
print(c)
help(time.strftime)
print(a)
x=time.strftime("%m/%d/%y")
print(x)
y="08 Auguest 2019"
s=time.strftime(y,"%d/%b%y")
print(s)