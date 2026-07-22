#Blocks of code that perform specific task

# function definition
def calc_mul(a,b): #parameters
    print(a*b)


v = calc_mul(3,4) #arguments ; function call
print(v)
calc_mul(5,50)

#default parameter

def cal_sum(a = 1,b = 1):
    return(a+b)

print(cal_sum())


# def cal_sum(a,b = 1):
  #  return(a+b)      (will give error)
# print(cal_sum())


def cal_sum(a ,b = 1):
    return(a+b)

print(cal_sum(1))

def cal_sum(a,b = 1):
    return(a+b)

print(cal_sum(1))

#def cal_sum(a = 1,b )
  #  return(a+b)        (will give error)

#print(cal_sum(1))

list1 = list(input("Enter a list:"))
def Len_List(list1):
    return(len(list1))

print(Len_List(list1))

list = [1,2,23,54,65,7,8]
def single_line(list):
    print(list)

single_line(list) 

#factorial

num = int(input("Enter a whole no.:"))
def fact(num):
    f = 1
    if num==0 or num== 1:
        print ("Factorial is 1")
    else:
        for i in range(1,num+1):
            f = f*i
        print(f)    
fact(num)            

d = float(input("Enter Dollar:"))
def rupee(d):
    r = d*90
    print(d,"Dollar eqaul to :",r,"rupee")
rupee(d)  

num = int(input("Enter a no.:"))
def check(num):
    if(num%2==0):
        print("Even")
    else:
        print("Odd")    
check(num)







 
