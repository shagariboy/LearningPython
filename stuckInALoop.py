secret_word = "chupacabra"
word = str(input("Please enter a something: "))

while word != " ":
    if word != secret_word:
        word = str(input("Please enter a something: "))
    else:
        break
print("You've successfully left the loop!")
   


 