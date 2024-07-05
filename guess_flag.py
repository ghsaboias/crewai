import random

# List of countries and their corresponding flags
flags = {
    "Canada": "🇨🇦",
    "France": "🇫🇷",
    "Germany": "🇩🇪",
    "Italy": "🇮🇹",
    "Japan": "🇯🇵",
    "Brazil": "🇧🇷",
    "United States": "🇺🇸",
    "United Kingdom": "🇬🇧",
    "Australia": "🇦🇺",
    "India": "🇮🇳"
}

def get_user_input(prompt):
    while True:
        answer = input(prompt).strip()
        if answer:
            return answer
        else:
            print("Input cannot be empty. Please try again.")

def play_round(score):
    country, flag = random.choice(list(flags.items()))
    print(f"Guess the country for the flag: {flag}")
    answer = get_user_input("Your answer: ")

    if answer.lower() == country.lower():
        print("Correct!")
        score += 3
    else:
        print(f"Wrong! The correct answer was {country}.")
        score -= 2

    print(f"Current score: {score}\n")
    return score

def flag_guessing_game():
    score = 0
    rounds = 5

    for _ in range(rounds):
        score = play_round(score)

    print(f"Game over! Your final score is: {score}")

    replay = get_user_input("Do you want to play again? (yes/no): ").lower()
    if replay in ("yes", "y"):
        flag_guessing_game()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    try:
        flag_guessing_game()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
