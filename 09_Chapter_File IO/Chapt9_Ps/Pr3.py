w = "Hele"
with open("Hey.txt","r") as j:
    c = j.read()
cn = c.replace(w,"Hello")

with open("Hey.txt","w") as j:
    j.write(cn)