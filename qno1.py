import json
my_file=open("qno1.json","r+")
j=json.load(my_file)
print(j)
my_file.close()
