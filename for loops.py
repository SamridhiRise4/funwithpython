# sequential traversal. For traversning list,string,tuple etc.

list =["Samriddhi Shukla","Lubna Anis","Neha Pandey"]
for i in list:
    print(i)

Str = "Hello World"
for i in Str:
    print(i)    

# for i in list :
#   some work
# else:
#   work when loop ends    

for i in Str:
    print(i)
else:
    print("Done!")    

list = [1,4,9,16,25,36,49,64,81,100]
for i in list:
    print(i)    

idx = 0
for i in list:
    if(i==36):
        print("Found at index",idx)
    idx+=1    

# range

print(range(8))    

for i in range(0,8,4):
    print(i)

for i in range(2,100,2):
    print(i)    

for i in range(1,101):
    print(i)   

for i in range(100,0,-1):
               print(i)   

n = int(input("Enter a whole no.:"))
for i in range(11):
     print(n*i)


#pass (It does nothing ,leave empty)

#for i in range(9):
     #nothing      (will give error)


for i in range(9):
     pass


sum = 0
n = 5
for i in range(1,n+1):
     sum = sum +i
print("The sum is",sum)     

#Factorial

num = int(input("Enter a whole no.:"))
fact = 1
if(num == 0 or num == 1):
     print("The factorial is 1" )
else :
     for i in range(1,num+1):
          fact = fact*i 

     print("The factorrial is :",fact)         

               
