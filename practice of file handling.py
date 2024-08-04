def check_by_line():
    word = "pyq"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1 
    f.close()
    return -1
print(check_by_line())