import random
from os import system, name
from time import sleep


keys = [1, 2, 3]
values = "Stone Paper Scissor".split()
elements = dict(zip(keys, values))
count, point, win, loose = 0, 0, 0, 0
Options = ["Continue", "Restart", "Stop Playing"]
Game_Options = dict(zip(keys, Options))


def clear():
    # for windows
    sleep(0.2)
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def retry():
    global count, point, win, loose
    while True:

        for key, value in Game_Options.items():
            print(f"[+] Press {key} then ENTER for {value} \n", end="")
        quarry = int(input("=>"))
        if quarry == 1:
            clear()
            return count, point, win, loose
        elif quarry == 2:
            clear()
            count, point, win, loose = 0, 0, 0, 0
            return count, point, win, loose
        elif quarry == 3:
            count = 10
            return count, point, win, loose
        else:
            print("[ERROR] Invalid input.\n enter (1 or 2 or 3)")
            continue


def Who_wins(x, y):
    if x == "Stone" and y == "Scissor":
        return True
    elif x == "Paper" and y == "Stone":
        return True
    elif x == "Scissor" and y == "Paper":
        return True
    elif x == y:
        return "Draw"
    else:
        return False


while count == 0:

    while count <= 9:
        print(f"[+]Round {count + 1}")
        try:
            # -------------> Genareting a random move for computer
            random_move = random.choices(values, weights=[33.333, 33.333, 33.333], k=1)

            # -------------> User is choosing move
            for key, value in elements.items():
                print(f"[+] Press {key} Then ENTER for {value} \n", end="")
            Choice = int(input("=> "))
            clear()
            My_move = elements[Choice]
            print(f"\n[+]Your Move => {My_move}")

            # -------------> Computer is choosing move
            Computer_move = random_move[0]
            print(f"[+]Computer's Move => {Computer_move}\n")

            # -------------> Calling Who_Win func for determine who will win
            Win_Truth = Who_wins(My_move, Computer_move)
            if Win_Truth == True:
                print("--->You Win<---\n")
                win = win + 1
                count = count + 1
                point = point + 100
                continue
            elif Win_Truth == False:
                print("--->Computer Win<---\n")
                loose = loose + 1
                count = count + 1
                point = point - 50
                continue
            elif Win_Truth == "Draw":
                print("--->Match Draw<---")
                count = count + 1
                point = point + 10
            else:
                print("[ERROR] Invalid Input !!!")
                retry()
        except:
            print("[ERROR] Invalid Input !!!")
            retry()

    # -------------> Your Result
    clear()
    print(f"[=>]Your Total Point Is {point}")
    print(f"[=>]Your Total Win Is {win}")
    print(f"[=>]Your Total Lose Is {loose}\n")
    retry()
input("Press any key to exit...\n")
