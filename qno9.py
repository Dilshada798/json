# Q.9 Apki pass ek shopping name ki ek dictionary hai

# {
#     "shopping_list":
#         { 
#             "chaco":"15",
#             "Biscuits":"50",
#             "Diary_milk":"30",
#             "ice_cream":"20",
#         } 
# }

import json
dict1={}
num=input("enter the no.of items:")
for i in range (len(num)):
    a=input("enter the items:")
    b=input("enter the quantity:")
    dict1.update({a:b})
with open("file9.json","w") as file:
    json.dump(dict1,file,indent=3)
