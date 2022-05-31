import random
import sys
import time
import os


def slow_print(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1.0 / 30)


if __name__ == "__main__":
    slow_print(
        "     Hi I am NAOMI."
        "\n      I'm gonna select a random number between 1-100 "
        "\n          Can you read my mind?"
        "\n              Tale me what is the number"
    )
n = random.randint(0, 100)
point = 100
count = -1
while True:

    point = point - 5
    count = count + 1
    number = int(input("Enter the number here:  "))

    if point < 0:
        os.system("cls" if os.name == "nt" else "printf '\033c'")
        slow_print(
            "                You tried a lot..!" "\n                    GAME OVER"
        )
        point = 0
        time.sleep(3)
        break
    elif 1 <= number < n:
        print("     No honey.. ")
        slow_print("\n      It is smaller" "\n          try a bigger number")
        continue
    elif 100 >= number > n:
        print("     No honey.. ")
        slow_print("\n      It is bigger" "\n          try a smaller number")
        continue
    elif n == number:
        slow_print(
            "     Ok.. you got my number.." "\n        You are my best friend..!"
        )
        break
    else:
        slow_print(
            "     Hey..!"
            "\n       My number is between 1 to 100"
            "\n           Are you Crazy...!"
            "\n               ...GAME OVER..."
        )
        point = -100
        break
os.system("cls" if os.name == "nt" else "printf '\033c'")
slow_print("                 FINAL SCORE" "         \nYour total point is:")
print("                ", point)
slow_print("         \nyour total played move is:")
print("                                   ", count)
input("\n" "\n" "\n.....press any key to exit")
