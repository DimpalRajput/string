# list
# #creating list
# # students=["anjali","minakshi","garima","sushant","deepak"]
# # print(students[3])
# # print(students)
# # #updating list
# # students[2]="sonali"
# # print(students)
# # #Tuple
# # #creating tuple
t1=(23,43,"sonakshi",57.8,43,43)
# # print(t1)
# # #slicing
# print(t1[1:3])
# #length
# print(len(t1))
# if "sonakshi" in t1:
#     print("name is present")
# else:
#     print("name is not present")
# #count
# print(t1.count(43))
# #index number
# print(t1.index(43))
# print(students[-3:-1])
# my_list=list(t1)
# my_list.remove(23)
# print(my_list)
# t1=tuple(my_list)
# print(t1)
# list3=[34,78,(23,78,67),98,100]
# print(len(list3))
# print(list3.append(65))
# value=(34,56.7,"priyal",67.8)
# print(value)
# list2=list(value)
# list2.pop()
# print(list2)
# value=tuple(list2)
# #print(value)


# value=((34,56.7,"priyal",67.8)*3)
# print(value)

# t3=value+t1
# print(t3)
#print(value.index("priyal"))
first=t1.index(43)
print(t1[first+1:].index(43)+first+1)







