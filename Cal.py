def add(n1 ,n2):
    return n1 + n2
def sub(n1 ,n2):
    return n1 - n2
def multi(n1 ,n2):
    return n1 * n2
def div(n1 ,n2):
    return n1 / n2

print("Enter the operation\n")
print("1 Add\n")
print("2 Subtract\n")
print("3 Multiply\n")
print("4 Divide\n")

select = int(input("Select operation from 1,2,3,4 : "))

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

if select == 1:
    print(num1 , "+" , num2 ,"=", add(num1,num2))
elif select == 2:
    print(num1 , "-" , num2,"=",sub(num1,num2) )
elif select == 3:
    print(num1 , "*" , num2,"=",multi(num1,num2) )
elif select == 4:
    print(num1 , "/" , num2,"=",div(num1,num2) )   
else:
    print("invalid input") 