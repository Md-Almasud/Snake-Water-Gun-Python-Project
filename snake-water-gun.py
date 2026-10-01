import random

def result_game(user, computer):

    if user == computer:
        return None
    
    # Snake vs Gun
    if user == "g" and computer == "s":
        return True
    if user == "s" and computer == "g":
        return False

    # Gun vs Water
    if user == "w" and computer == "g":
        return True
    if user == "g" and computer == "w":
        return False

    # Water vs Snake
    if user == "s" and computer == "w":
        return True
    if user == "w" and computer == "s":
        return False

rand_no = random.randint(1,3)

print("Computer's Turn: Snake(s), Water(w), Gun(g): ")
if rand_no == 1:
    computer = "s"
elif rand_no == 2:
    computer = "w"
else:
    computer = "g"
    
user = input("Your Turn: Snake(s), Water(w), Gun(g): ").lower()

result = result_game(user, computer) #Returns True if you win, False if you lose, None for Draw,

print(f"\nYou Chose: {user}")
print(f"\nComputer Chose: {computer}\n")
    
if result is None:
        print("It's a draw.")
elif (result):
        print("You Win.")
else:
        print("You Lose.")