#Loops are used to repeat instructions
i = 0
while i<=4 :
    print("Samriddhi Shukla")
    i+=1
print(i)

i = 1
while i<=10:
    print(i)
    i+=1

i = 10 
while i>=0:
    print(i)
    i-=1

# Num from 1 to 100

num = 1
while num<=100:
    print(num)
    num+=1    

#Num from 100 t 1

num = 100
while num>=0:
    print(num)
    num-=1

# Multipkication Table

n = int(input("Enter a Whole no. :"))
i = 1
while i<=10:
    print(n*i)
    i +=1

list = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(list):
    print(list[idx])
    idx+=1


s = 36
i =0 
while i<len(list):
    if(list[i]==s):
        print("Found at index :",i)
    i+=1    

# Break

i =0
while i<=4:
    if i ==3 :
        break
    print(i)   
    i+=1

#continue

i = 0
while i <= 5:
    if(i==3):
        i+=1
        continue #skip
    print(i)
    i+=1 

# print odd skip even

i = 0
while i <= 10:
    if(i%2==0):
        i += 1
        continue
    print(i)
    i += 1    

#sum of first n numbers


    









