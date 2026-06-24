name="jaanvi"#global scope
def function():#local scope
    global age
    age=20
    print(age)
function()
print("hello",name)
 #data type : 1 numerical data type:integer,float,complex
x=20
y=10.5
print(type(x))
print(type(y))
z=complex(x)
print(z)
r=int(y)
print(r)
h=5+3j
print(type(h))
message=" Hello khushbu this is python program "
print(len(message))
print(message[:-1])
print(message.lower())
print(message.replace("jaanvi","mahak"))
if("mahak" in message):
 print("mahak is present in message")
else:
   print("not present in message")
   print(message.strip())