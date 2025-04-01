travelling=input("yes or no:")
while travelling=='yes':
    num=int(input("number of people travelling:"))
    for num in range(1,num+1):
        name=input("Name:")
        age=input("age:")
        sex=input("male or female:")
        print(name)
        print(age)
        print(sex)
        travelling=int(input("oops! forgot someone"))