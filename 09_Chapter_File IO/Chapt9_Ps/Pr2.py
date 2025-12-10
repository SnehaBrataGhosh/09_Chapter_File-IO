def genTab(n):
    Table = ""
    for i in range(1,11):
        Table += f"{n} X {i} = {n*i}\n"
    with open(f"Tables/Table_{n}.txt", "w") as j:
        j.write(Table)
    

for i in range(1, 30):
    genTab(i)
