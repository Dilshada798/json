# Q7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai?
import json
file="Txt.txt"
dict={}
a=open(file)
for i in a:
    key,dictationary=i.split(None,1)
    dict[key]=dictationary.strip()
new_file=open("question 7.json","w")
json.dump(dict,new_file,indent=4)
new_file.close()


