f = open("samle.txt", "a")
f.write("\nThis is new line")
f.close()
 

with open("demo.txt", "w") as t:
    t.write("Ali is good")
import os
os.remove("demo.txt")    