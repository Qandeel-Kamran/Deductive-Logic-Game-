import random

def generate_secret_number():
    digits = list("0123456789")
    random.shuffle(digits)
    return ''.join(digits[:3])

def get_feedback(secret, guess):
    feedback = []
    for i in range(3):
        if guess[i] == secret[i]:
            feedback.append("👌")  # Correct digit and position
        elif guess[i] in secret:
            feedback.append("👍")  # Right digit, wrong position
        else:
            feedback.append("❌")  # Not in secret
    return feedback

def surprise_sticker():
    stickers = [
        "🎉🎁 You won! Here's a virtual hug: (づ｡◕‿‿◕｡)づ",
        "🐱 You did it! Enjoy this cat: =^.^=",
        "🌈 Woohoo! Have a rainbow: 🌈🌟💖",
        "🍰 Congrats! Here's a slice of cake: [🍰]",
        "🐸 You guessed it! Here's Froggy cheering for you: (•‿•) 🐸"
    ]
    print("\n" + random.choice(stickers))

def play_game():
    secret_number = generate_secret_number()
    attempts = 10

    print("🎮 Welcome to the Deductive Logic Game!")
    print("Guess the 3-digit secret number. You have 10 tries.")
    print("Feedback: 👌 = correct spot, 👍 = right digit/wrong spot, ❌ = wrong digit\n")

    for attempt in range(1, attempts + 1):
        valid_input = False
        retries = 0

        while not valid_input:
            guess = input(f"🔢 Attempt {attempt}: Enter a 3-digit number: ").strip()
            if guess.isdigit() and len(guess) == 3 and len(set(guess)) == 3:
                valid_input = True
            else:
                print("⚠️ Invalid input. Enter a 3-digit number with **non-repeating** digits.")
                retries += 1
                if retries >= 5:
                    print("🚫 Too many invalid attempts. Game over.")
                    return

        feedback = get_feedback(secret_number, guess)
        print("🧩 Feedback:", ' '.join(feedback))

        if feedback == ["👌", "👌", "👌"]:
            print("\n🎉 You Got IT! Congratulations!")
            surprise_sticker()
            break
    else:
        print(f"\n💔 Sorry, you're out of attempts. The number was {secret_number}.")

def main():
    while True:
        play_game()
        again = input("\n🔁 Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("👋 Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()

