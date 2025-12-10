# This programme reads from file

def read_full():
    file = open("sample.txt", "r")
    content = file.read()
    print("== Full content using read() ==\n", content)
    file.close()

def read_line_by_line():
    file = open("sample.txt", "r")
    print("\n== First line using readline() ==")
    print(file.readline())
    file.close()

def read_all_lines():
    file = open("sample.txt", "r")
    lines = file.readlines()
    print("\n== All lines using readlines() ==")
    for line in lines:
        print(line.strip())
    file.close()

read_full()
read_line_by_line()
read_all_lines()
