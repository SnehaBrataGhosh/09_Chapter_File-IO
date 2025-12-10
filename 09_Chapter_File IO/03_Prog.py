# This programme does reading and writing a file using with statement
def write_with():
    with open("with_sample.txt", "w") as file:
        file.write("This file uses the 'with' statement.\n")
        file.write("It automatically handles file closing.\n")
    print("== Written to with_sample.txt using with-statement ==")

def read_with():
    with open("with_sample.txt", "r") as file:
        print("== Reading using with-statement ==")
        print(file.read())

write_with()
read_with()
