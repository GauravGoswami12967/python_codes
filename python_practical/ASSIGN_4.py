def swapNumbers(a,b):
    temp=a
    a=b
    b=temp
    return a,b
def swapNumberstwo(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b

# num1=int(input("enter your number for a : "))    
# num2=int(input("enter your number for b : "))    
# res1,res2=swapNumbers(num1,num2)
# print(f" a is {res1} now and b is {res2} ..")

num1=int(input("enter your number for a : "))    
num2=int(input("enter your number for b : "))    
res1,res2=swapNumberstwo(num1,num2)
print(f" a is {res1} now and b is {res2} ..")
