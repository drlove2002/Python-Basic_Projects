# Design a calculator which will correctly solve all the problems except the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Rule :- Your program should take operator and the two numbers as input from user and then return the result
print("[1]Division(/)\n"
      "[2]Multiplication(*)\n"
      "[3]Addition(+)\n"
      "[4]Subtraction(-)\n"
      "Enter choice(/ or * or + or -)\n")
select = str(input())
print("Enter 1st number")
no1 = int(input())
print("Enter 2st number")
no2 = int(input())
print(no1, select, no2, "=")
if no1 == 45 and select == "*" and no2 == 3:
    print("555")
elif no1 == 56 and select == "+" and no2 == 9:
    print("77")
elif no1 == 56 and select == "/" and no2 == 6:
    print("4")
else:
    if select == "/":
        print(float(no1 / no2))
    elif select == "*":
        print(float(no1 * no2))
    elif select == "+":
        print(float(no1 + no2))
    elif select == "-":
        print(float(no1 - no2))
    else:
        print("getting an ERROR! Please check and try again")
