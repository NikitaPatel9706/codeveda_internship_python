

#basic calculator
def add(a,b):
        return a+b
def subtraction(a,b):
        return a-b
def multiplication(a,b):
       return a*b
def division(a,b):
   if (b==0):
       print("can't divide by zero")
   return a/b

print("basic calculator")
print("select the below operation to perform task:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Divison")

choice=input("enter the choice(1/2/3/4): " )
num1=float(input("enter the First Number:  "))
num2=float(input("enter thr second number:"))

if choice=="1":
    print("result:",add(num1,num2))
elif choice=='2':
   print("result:",subtraction(num1, num2)) 
elif choice=="3":
    print("result:",multiplication(num1, num2))
elif choice=="4" :
    print("result:",division(num1, num2))
else :
   print("invalid choice")    
    
        