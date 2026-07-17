#1.
def calculate(a,b=5):
    return a+b,a*b
x,y=calculate(4)
print(x,y)
print(calculate(4,2)[1])
#2.
def display(a,b,c=10):
    print(a,b,c)
display(1,c=3,b=2)
display(4,5)
#3.
def calculate(number):
    if number%2==0:
     return number//2
    print("odd number")
    return number*3
print(calculate(8))
print(calculate(5))
#4.
def add_item(item,container=[]):
   container.append(item)
   return container
print(add_item(1))
print(add_item(2))
print(add_item(3,[]))
print(add_item(4))
#5.
def analyse(first,*values):
   return first,max(values),sum(values[::2])
print(analyse(10,3,8,5,2))
#6.
def build_record(**data):
   data["total"]=sum(
      value
      for value in data.values()
      if isinstance(value,int)
      )
   return sorted(data.items())
print(build_record(a=2,b=3,name="x"))
#7.
def calculate(a,b,c):
   return a+b+c
values=(2,3)
options={"c":4}
print(calculate(*values,**options))
#8.
def report(name,*,score=0,passed=True):
   return f"{name}:{score}:{passed}"
print(report("riya",score=88))
print(report("kabir",passed=False,score=40))