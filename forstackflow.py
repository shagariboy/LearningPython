secret_Level = "chupacabra"
input("Please enter a something: ")

while secret_Level == True:
    word = str(input("Please enter a something: "))
    if word != secret_Level:
        print(str(input("Please enter a something: ")))
    else:
        break
    print("You've successfully left the loop!")