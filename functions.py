#1.
def hello(a):
    return a;
result=hello("hello world")
print(result)
#2.
def name():
    print("dimpal")
result=name()
#3.
def number():
    n=1
    while n<=10:
        print(n)
        n+=1
result=number()
#4.
def numbers():
    n=10
    while n>=1:
        print(n)
        n-=1
result=numbers()
#5.
def even():
    n=1
    while n<=10:
     if n%2==0:
        print(n)
     n+=1
even() 
#6.
def square(a):
    return a*a
result=square(6)
print(result) 
#7.
def cube(a):
    return a*a*a
result=cube(4)
print(result)
#8.
def add(a,b):
    return a+b
result=add(34,56)
print(result)
#9.
def comparison(a):
    if a%2==0:
        print("a is even")
    else:
        print("a is odd")   
comparison(34) 
#10.
def number1(a):
    if a>0:
        print("a is positive")
    if a<0:
        print("a is negative")
    else:
        print("a is zero")
number1(-56)
#11.
def divisibility(a):
    if a%5==0:
        print("divisible by 5")
    else:
        print("not divisible by 5")
divisibility(45)
#15.
def factorial(n):
    fact=1
    while n>=1:
        fact=fact*n
        n-=1
        print(fact)
factorial(10)        





