import csv 
file =  open("Person.csv", "w", newline="") 
new = csv.writer(file)
new.writerow(["Name","Experience (years)","Projects Completed"])
new_data = []
while True:
    n = input("Enter name: ")
    e = int(input("Enter Experince: "))
    p = int(input("Enter project completed: "))
    fst = [n,e,p]
    new_data.append(fst)
    ch = input("Do you want to enter more data? Y/N: ")
    if ch == "n" or ch == "N":
        break
for i in new_data:
    new.writerow(i)
file.close()

check = open("Person.csv", "r")
for i in check:
    print(i)
check.close()