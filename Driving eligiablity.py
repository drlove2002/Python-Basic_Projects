print("Please enter your age \nTo verify your eligibility og Driving license \n")
age = int(input())
if 7 < age < 18:
    print("Sorry you are not eligible\n")
elif age == 18:
    print("We cannot suggest you now \n you have to come in your office physically ")
elif 100 > age > 18:
    print("Congratulation! you're eligible")
else:
    print("Unexpected error \n Please only enter you age as a number")
