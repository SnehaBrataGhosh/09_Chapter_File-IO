with open("log.txt","r") as j :
    c  = j.read()

if("python" in c):
    print("Good news the word Python is present")
else:
    print("Bad news the word Python is not present")
