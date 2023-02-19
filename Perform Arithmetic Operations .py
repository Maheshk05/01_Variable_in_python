num1 = eval(input("Enter 1st no:"))
num2 = eval(input("Enter 2nd no:"))

N = str(input("+ / - /*  // :"))

if N == "+":
    t = num1 + num2
    print(f"Addition of {num1} and {num2} is ",t)
    
elif N == "-":
    t = num1 - num2
    print(f"subtraction of {num1} and {num2} is ",t)

elif N == "*":
    t = num1 * num2
    print(f"multiplication of {num1} and {num2} is",t)

elif N == "/":
    t = num1 / num2
    print(f"division of {num1} and {num2} is",t)

else:
    print("plz enter valid operator")
    
    
    
    
