num=int(input("enter the numerator:"))
demo=int(input("enter the denominator:"))
try:
    quo=num/deno
    print("QUOTIENT:",quo)
except ZeroDivisionError:
    print("Denominator cannot be zero")