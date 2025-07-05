import random 

def number_guessing_game():
     print("Hi guess number between 1-100")

     secret_number=random.randint(1,100)
     attempt=0

     while True:
          try:
               guess=int(input("Enter the guessing number:"))
               attempt+=1

               if guess < 1 or guess > 100 :
                    print("Enter number between 1 to 100")
                    continue
               if guess < secret_number:
                    print("Number is low:Try again")
               elif guess > secret_number:
                    print("the number is High : Try again") 
               else:
                    print("The number is correct")
          except ValueError:
               print("Enter the correct  input")
number_guessing_game()