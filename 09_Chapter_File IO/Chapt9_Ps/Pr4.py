w = ["Hele" , "He"]
with open("Hey.txt","r") as j:
    c = j.read()

for wo in w:
    c = c.replace(w,"Hello")

with open("Hey.txt","w") as j:
    j.write(c)