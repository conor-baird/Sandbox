name = input("Name: ")
letters = 0
for letters in range(len(name)):
    if letters % 2:
        print(str(letters))

    elif len(name) == 0:
        print("Error Blank")