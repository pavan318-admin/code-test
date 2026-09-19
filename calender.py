def add(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "cannot divide by zero"
        return a/b

print("python calculator")
print("-----------------")

a = float(input("enter first number:"))
b = float(input("enter second number:"))

print("\n results:")
print("addition:",add(a,b))
print("subtractiond:",subtraction(a,b))
print("multiplication:",multiplication(a,b))
print("division:",divide(a,b))