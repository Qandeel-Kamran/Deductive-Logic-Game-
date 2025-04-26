# Deductive-Logic-Game
This Python program is a fun deductive logic game where the player tries to guess a randomly generated 3-digit number with non-repeating digits. Let’s break it down step-by-step:

🔧 1. Function: generate_secret_number()
python
Copy
Edit
def generate_secret_number():
    digits = list("0123456789")
    random.shuffle(digits)
    return ''.join(digits[:3])
Purpose: Generates a secret 3-digit number.

How:

Takes digits 0–9 and shuffles them randomly.

Selects the first 3 shuffled digits (ensuring no repeats).

Returns them as a string (e.g., '849').

🔍 2. Function: get_feedback(secret, guess)
python
Copy
Edit
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
Purpose: Gives feedback on the player's guess.

Feedback meaning:

👌 = Correct digit in the correct position.

👍 = Digit exists but in the wrong position.

❌ = Digit not in the secret number at all.

🎉 3. Function: surprise_sticker()
python
Copy
Edit
def surprise_sticker():
    stickers = [...]
    print("\n" + random.choice(stickers))
Purpose: Celebrates when the player wins with a fun message or emoji.

How: Picks one of several fun strings randomly and displays it.

🎮 4. Function: play_game()
This is the main game loop:

Generates the secret number.

Allows the user 10 attempts to guess it.

On each attempt:

Prompts the user for input.

Validates that the input is a 3-digit number with non-repeating digits.

Gives feedback using get_feedback().

Ends early if the player guesses correctly.

If the player guesses the number:

Celebrates with surprise_sticker().

If they fail all 10 tries:

Reveals the correct number.

Also protects against invalid input with up to 5 retries.

🏁 5. Function: main()
python
Copy
Edit
def main():
    while True:
        play_game()
        again = input("\n🔁 Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("👋 Thanks for playing! Goodbye.")
            break
Keeps the game going until the user says they want to stop (n).

Calls play_game() repeatedly until then.

🧠 Summary:
You’re playing a logic puzzle where:

The computer picks a unique 3-digit number.

You try to deduce it from feedback.

You get up to 10 chances per round.

Cute emojis and messages add a fun twist.
