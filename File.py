# operations on files
import os
f = open("Sets.py","r")
print(f.read())
print(type(f.read()))
f.close()



f = open("List","r")
data = f.readline()
print(data)


f = open("heelo.txt","w") #truncate the whole file then write 
f.write("Haaaaaaa")
f.close()


f = open("heelo.tx","a")
f.write("\nI'm having a lot of fun")
f.close()

#with syntax

with open("Tuple.py","r") as f:
    data = f.read()
    f.close()

os.remove("heelo.txt")    

f = open("sample.txt","w")
f.write("Hi Everyone \n we are learning File I/O \n using Java \n I like programming in Java")
f.close()

with open("sample.txt","r") as f:
    data = f.read()
n = data.replace("Java","Python")
print(n)    

with open("sample.txt","w") as f:
    f.write(n)

    


