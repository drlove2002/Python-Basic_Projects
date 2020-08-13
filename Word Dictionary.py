# This is a dictionary tool to find word meaning
words = {"ball": "it is a round shaped object",
         "door": "it is a object help to enter into room",
         "chair": "it is a object you can sit on it"}

print("\n\nThis is a Word Dictionary app."
      "\nBut it has a certain amount of words to view.")
val = str(input("\nTo view all words *press 1*\nOr Enter the word that you want to know\n"))
if val == "1":
    print(words.keys())
elif val in words:
    print("Ok This is the meaning of your word")
    print(words.get(val))
else:
    print("Error")
