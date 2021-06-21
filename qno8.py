
import json


list1=["neelam","programer","24","2400",]
list2=["komal","trainer","24","20000"]
list3=["anuradha","HR","25","40000"]
list4=["Abhishek","manager","29","63000"]  
emp1={}
emp2={}
emp3={}
emp4={}
key=["name","designation","age","salary"]

dict={"emp1":emp1,"emp2":emp2,"emp3":emp3,"emp4":emp4}

for a in range(len(list1)):
    emp1.update({key[a]:list1[a]})
    emp2.update({key[a]:list2[a]})
    emp3.update({key[a]:list3[a]})
    emp4.update({key[a]:list4[a]})
with open("fil_e8.json","w")as k:
    json.dump(dict,k,indent=5)
   