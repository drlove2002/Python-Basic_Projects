# Health Management System

Client_list = {1: "Harry", 2: "Rohan", 3: "Hammad"}
Event_list = {1: "Exercise", 2: "Diet"}


def getdate():
    import datetime
    return datetime.datetime.now()


try:
    print("Select Client Name:")
    for key, value in Client_list.items():
        print("Press", key, "for", value, "\n", end="")

    client_name = int(input())

    print("Selected Client : ", Client_list[client_name], "\n", end="")
    print("Press 1 for Lock")
    print("Press 2 for Retrieve")

    Event = int(input())

    if Event is 1:
        for key, value in Event_list.items():
            print("Press", key, "to lock", value, "\n", end="")

        lock_name = int(input())

        print("Selected Job : ", Event_list[lock_name])

        f = Event(Client_list[client_name] + "_" +
                  Event_list[lock_name] + ".txt", "a")

        k = 'y'

        while(k is not "n"):

            print("Enter", Event_list[lock_name], "\n", end="")
            my_text = input()
            f.write("[ " + str(getdate()) + " ] : " + my_text + "\n")
            k = input("ADD MORE ? y/n:")
            continue
        f.close()

    elif Event is 2:

        for key, value in Event_list.items():

            print("Press", key, "to retrieve", value, "\n", end="")

        lock_name = int(input())

        print(Client_list[client_name], "-",
              Event_list[lock_name], "Report :", "\n", end="")

        f = Event(Client_list[client_name] + "_" +
                  Event_list[lock_name] + ".txt", "rt")

        contents = f.readlines()

        for line in contents:

            print(line, end="")
        f.close()
    else:

        print("Invalid Input !!!")

except Exception as e:

    print("Wrong Input !!!")
