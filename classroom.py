student_result=()
print("student_result:",)
marksheet={
        "student1":{"name":"shashank",
        "roll no.":1,
        "marks":[67,78,89,56,98],
        },
        "student2":{
        "name":"riddhi",
        "roll no.":2,
        "marks":[45,78,67,90,56]
        },
        "student3":{
        "name":"sashi",
        "roll no.":3,
        "marks":[34,78,67,95,57],
        },
        "student4":{
        "name":"priyanshu",
        "roll no.":4,
        "marks":[59,78,56,84,95],
        },
        "student5":{
        "name":"rishi",
        "roll no.":5,
        "marks":[48,94,50,64,83]
        }
}
if all("marks">100 and "marks"<0 for marks in marksheet):
    print("invalid marks")
else:
    print("valid marks")
