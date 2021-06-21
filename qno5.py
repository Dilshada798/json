# Q5.Json string ko check karo ki bo complex object contain karti hai ya nahi?

import json
def num_complex(a):
    if isinstance(a,complex):
        print(type(a))
        return("real",a.real,"imag",a.imag)
    json.dumps(a,indent=3)
print(num_complex(12+3j))

