



print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
number = int(input("Enter an integer number: "))
secret_number = 777
while number != 0:
    if number != secret_number:
        print("Ha ha! You're stuck in my loop!")
        number = int(input("Try again!: "))

    else:
        print("Well done, muggle! You are free now.")  
        number = int(input("Enter 0 to stop!: "))
  

