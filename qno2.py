# Q.2 Python object ko json data main convert karne ka program likho?

import json
a={"name":"david","class":"I","age":"6"}
file=open("file.json","w")
n=json.dumps(a)
json.dump(a,file,indent=4)
file.close()

