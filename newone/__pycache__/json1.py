import json
s={"1":"a","2":"b","3":"c"}
print(type(s))
v=json.dumps(s)
print(type(v))
l=json.loads(s)
print(type(l))