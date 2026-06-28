list
#creating list
students=["anjali","minakshi","garima","sushant","deepak"]
print(students[3])
print(students)
#updating list
students[2]="sonali"
print(students)
#Tuple
#creating tuple
t1=(23,43,"sonakshi",57.8,43,43)
print(t1)
#slicing
print(t1[1:3])
#length
print(len(t1))
if "sonakshi" in t1:
    print("name is present")
else:
    print("name is not present")
#count
print(t1.count(43))
#index number
print(t1.index(43))

