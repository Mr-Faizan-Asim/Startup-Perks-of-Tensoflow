import random

def number_guessing_game():
    cod = random.randint(1,100)
    attempt = 0
    while True:
        guess = int(input("Enter Any Number Between 1 to 100: "))
        attempt += 1
        if guess == cod:
            print("Congratulations! You did it")
            break
        elif guess > cod:
            print("To High :-(")
        else: 
            print("To Low :-(")

if __name__ == "__main__":
    number_guessing_game()

