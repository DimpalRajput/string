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
def add(*numbers):
    total=0
    for num in numbers:
        total+=num
    return total 
print(add(34,56,89,67))
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
#16.
def attendance(present,*num ):
    for num in num:
        print(present,num)
attendance("present",1,2,4,5,6)
#17.
# def show_detail(**details)
# for key,value in details.items():
#17. create_profile(**user):
    # print("user profile")
    # print("name:",user.get("name"))
    # print("city:",user.get("city"))
    # print("email address:",user.get("email address"))
# create_profile("priya","nimrana","priya1234@gmail.com")
#18.
def add(a:int,b:int)->int:
    return a+b
print(add(6,8))
#map,filter,sorted
def find_largest(numbers):
    largest=numbers[0]
    for number in numbers:
        if number>largest:
            largest=number
        return largest
find_largest=[67,78,99,56,45]


    




 
      





