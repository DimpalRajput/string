#1.
x=10
x=str(10)
print(x*2,type(x))
#2.
value="5.8"
number=float(value)
print(int(number),bool(number),type(number))
#3.
x=10
def show():
    x=20
    print(x,end=" ")
    
show()
print(x)
#4.
count=5
def update():
    global count
    count+=3
update()
print(count)
#5.
text="python"
print(text[1],text[-1],text[1:5:2])
#6.
text1="PyThOn"
clean=text1.strip()
print(clean.lower(),clean.upper())
#7.
text2="banana"
print(text2.replace("a","o",2),text2.count("an"))
#8.
text3="red,green,blue"
parts=text3.split(",")
print("-".join(parts),len(parts))
#9.
text="intern_python.py"
print(text.find("python"),text.startswith("intern"),text.endswith(".py"))
#10.
code="python3"
year="2026"
print(code.isalpha(),code.isalnum(),year.isdigit())
#11.
numbers=[1,2,3]
numbers.append([4,5])
print(numbers)
#12.
numbers1=[1,2,3]
numbers1.extend((4,5))
print(numbers1)
#13.
values1=[10,30]
values1.insert(1,20)
print(values1)
#14.
numbers2=[1,2,3,2]
numbers2.remove(2)
print(numbers2)
#15.
numbers3=[10,20,30]
value=numbers3.pop(1)
print(value,numbers3)

