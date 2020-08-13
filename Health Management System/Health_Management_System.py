#  -----------> Health Management System <--------------
# 3 Clients - Harry, Rohan, Hammed
# 3 files - For add data to log file
# 3 files - For retrive data from log file
# Total 6 files
# create function for datetime
# Health Management System

Client_list = {1: "Harry", 2: "Rohan", 3: "Hammad"}
Event_list = {1: "Exercise", 2: "Food"}


def getdate():
    import datetime
    return datetime.datetime.now()


try:
    print("Select Client Name:")
    for key, value in Client_list.items():
        print("[+] Press", key, "for", value, "\n", end="")

    client_name = int(input("=>"))

    print("[INFO] Selected Client : ", Client_list[client_name], "\n", end="")
    print("[+]Press 1 for Add Notes")
    print("[+]Press 2 for Watch History log")

    Event = int(input("=>"))

    if Event == 1:
        for key, value in Event_list.items():
            print("[+] Press", key, "to Add Notes for", value, "\n", end="")

        lock_name = int(input("=>"))

        print("[INFO] Selected Event : ", Event_list[lock_name])
        f = open(Client_list[client_name] + "_" +
                 Event_list[lock_name] + ".txt", "a")
        k = "y"

        while(k != "n"):

            print("Enter", Event_list[lock_name], "\n", end="")
            my_text = input()
            f.write("[ " + str(getdate()) + " ] : " + my_text + "\n")
            k = input("[INFO] ADD MORE ? y/n:")
            continue
        f.close()

    elif Event == 2:

        for key, value in Event_list.items():

            print("[+] Press", key, "to retrieve", value, "\n", end="")

        lock_name = int(input("=>"))

        print("[INFO] ", Client_list[client_name], "-",
              Event_list[lock_name], "Report :", "\n", end="")

        f = open(Client_list[client_name] + "_" +
                 Event_list[lock_name] + ".txt", "rt")

        contents = f.readlines()

        for line in contents:

            print(line, end="")
        f.close()
    else:

        print("[ERROR] Invalid Input !!!")

except Exception as e:

    print("[ERROR] Wrong Input !!!")
