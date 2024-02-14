import re
txt ="The rain in spain"
x= re.search("^The.*spain$",txt)
if x:
    print("yes")
else:
    print("no")