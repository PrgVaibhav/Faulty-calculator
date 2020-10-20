# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:

print("Calculator by Vaibhav")
print("Enter your first number: ")
num1 = int(input())
print("Enter your second number: ")
num2 = int(input())
print("So what you wanna do\n"
      "+ for addition\n"
      "- for substraction\n"
      "* for multiplication\n"
      "/ for division\n")
num3 = input()

if num1==56 and num2==9 and num3=='+':
    print("Your answer is 77")

elif num3=='+':
    print(num1+num2)

if num1==45 and num2==3 and num3=='*':
    print("Your answer is 555")

elif num3=='*':
    num4=num1*num2
    print(num4)

if num1==56 and num2==6 and num3=='/':
    print("Your answer is 4")

elif num3=='/':
    div=num1/num2
    print(div)

elif num3=='-':
    sub=num1-num2
    print(sub)
