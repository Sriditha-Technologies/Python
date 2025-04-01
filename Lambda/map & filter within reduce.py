r=reduce(lambda x,y:x+y, map(lambda x:x+x, Filter(lambda x:(x<=4),[1,2,3,4,5,6])))
print(r)