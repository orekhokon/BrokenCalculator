print("If you want to add two numbers please type '+'"
      "if you want to divide two numbers please type '/'"
      "if you want to substract two numbers please type '-'"
      "if you want to multiply two numbers please type '*'")
a = input("What do you want to do")
num1 = int(input("Write your first number"))
num2 = int(input("Write your second number"))
if num1==45 and num2==3 and a=="*":
    print(7)
elif num2==45 and num1==3 and a=="*":
    print(7)

elif a == "+":
    print(num2+num1)
elif a == "*":
    print(num1*num2)
elif a == "/":
    print(num1/num2)
elif a == "-":
    print(num1-num2)
else:
    print("Don't you fuck with me now kid")