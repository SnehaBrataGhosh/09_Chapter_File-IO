# This programme writes the file and writes in the file

def write_new():
    file = open("output.txt", "w")
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    file.close()
    print("== Content written using write() ==")

def append_text():
    file = open("output.txt", "a")
    file.write("This line is appended.\n")
    file.close()
    print("== Content appended using append mode ==")

def write_multiple_lines():
    lines = ["Line A\n", "Line B\n", "Line C\n"]
    file = open("output.txt", "w")
    file.writelines(lines)
    file.close()
    print("== Multiple lines written using writelines() ==")

write_new()
append_text()
write_multiple_lines()
