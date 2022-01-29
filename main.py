import art
import random
print(art.logo)

answer = random.randint(1,100)

lives_hard = 5
lives_easy = 10
difficulty_mode = input("Choose easy or hard: ").lower()

def guessing_game(lives):
    if difficulty_mode == "easy":
        lives = lives_easy
    else:
        lives = lives_hard
    return lives

def game():
    game_lives = guessing_game(difficulty_mode)
    is_alive = True
    while is_alive:
        player_guess = int(input("Choose a number between 1 and 100: "))
        if player_guess != answer:
            if player_guess > answer and game_lives != 1:
                print("Guess lower")
            elif player_guess < answer and game_lives != 1:
                print("Guess higher")
            game_lives -= 1
        if game_lives == 0:
            print(f"Game over! The correct answer was {answer}")
            is_alive = False
        elif player_guess == answer:
            print(f"That's right! The correct answer was {answer}")
            is_alive = False
    go_again = input("Do you want to play again? Y or N: ").lower()
    if go_again == "y":
        game()
    else:
        print("Thank you for playing! Goodbye!")

game()