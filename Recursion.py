# When function call itself

# Loops and Recursion is interrelated 
# The same work may be donr by both (loops & recursion)

def check(n):
    if n == 0: #base case
        return
    print(n)
    check(n-1)  #call stack
check(7)

#factorial 

def fact(n):
    if (n == 0 or n ==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(5))    

#sum of first n numbers

def sum(n):
    if n ==0:
        return 0
    return sum(n-1)+n
print(sum(5))

# print all elements in a list

def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

name = ["a","b","c"]    
print_list(name)




