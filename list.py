# list
# #creating list
# students=["anjali","minakshi","garima","sushant","deepak"]
# print(students[3])
# print(students)
# # #updating list
# students[2]="sonali"
# print(students)
# # #Tuple
#  #creating tuple
# t1=(23,43,"sonakshi",57.8,43,43)
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
#list3=[34,78,(23,78,67),98,100]
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
# print(value.index("priyal"))
#print(list3[::-1])

#allow only unique elememts
#name={"shruti","priyanka","neer","bhanu","shruti",9,67.8,0,False,"sudhanshu",56}
#print(name)
#finding length
#print(len(name))
#data type
#print(type(name))
#tuple1=("riddhi","priyal",56,78.9,True,"sudhanshu")
#t1=set(tuple1)
#print(t1)
#set2= {}
#print(type(set2))
#print(set2)
#print("riddhi" in name)
#print("shruti" not in name)
#for priyanka in name:
    #print("priyanka")
#name.add("siddhart")
#print(name)
#name.update(t1)
#print(name)
#name.remove("neer")
#print(name)
#name.discard("priyanka")
#print(name)
#union,update,intersection and other methods
#set3=name.union(t1)
#print(set3)
#name.update(t1)
#print(name)
#set4=name.intersection(t1)
#print(set4)
#name.update(list3)
#print(name)
#l1=["dimpalrajput7474@gmail.com","rinkumittal98@gmail.com","dimpalrajput7474@gmail.com","rinkumittal98@gmail.com"]
#s1=set(l1)
#print(s1)
marketing={
   "ITEM1":{"product":"mobile phone",
    "sale":156,
    "profit":"12 lakh"},
    
    "ITEM2":{"product1":"laptop",
        "sale1":325,
        "profit1":"25 lakh"},

    
    
    "ITEM3":{"product2":"tablet",
        "sale2":234,
        "profit2":"13 lakh"},
    
}
marketing.get("product4")
print("product is not present")

#print(marketing)
#print(len(marketing))
#production=dict(item="laptop",total=34)
#print(type(production))
#print(production)
#l2=[("name","sonakshi"),("height",5.2),("age",13),("t1",(23,45,67)),("value",True)]
##dict1=dict(l2)
#print(dict1)
#print(type(dict1))
#to check existance of key through sqaure brackets and get method and print a message in get method
#marketing.update({"discount":"5%",
                 #"branch":"new delhi"})
#print(marketing)
#print(marketing.popitem())
#print(marketing)
#clear,delete
python={"naveen","garima","mahima","preeti","janvi"}
java={"janvi","sumit","naveen","punit"}
set1=python.intersection(java)
#print(set1)
#print(marketing.copy())





