import random
import time
import threading

# Console formatting
BLACK_BG = '\033[40m'
NEON_GREEN = '\033[92m'
NEON_CYAN = '\033[96m'
NEON_RED = '\033[91m'
BOLD = '\033[1m'
ENDC = '\033[0m'

GREEN = NEON_GREEN
BLUE = NEON_CYAN
RED = NEON_RED


def main():
    # Difficulty settings
    modes = {"easy": "Easy", "medium": "Medium", "hard": "Hard"}

    print(BLACK_BG + BLUE + BOLD + "\n🎮 WELCOME TO HACKER'S VAULT\n" + ENDC)
    print(
        NEON_GREEN
        + "   Dark neon missions. Black market terminals. One code at a time.\n"
        + ENDC
    )

    # Difficulty selection
    while True:
        hacker_mode_input = input(
            "Choose difficulty (Easy, Medium or Hard): "
        ).strip().lower()

        if hacker_mode_input in modes:
            hacker_mode = modes[hacker_mode_input]
            break
        else:
            print(
                RED
                + "❌ Invalid input. Please choose Easy, Medium, or Hard."
                + ENDC
            )

    # Mode feedback
    if hacker_mode == "Easy":
        print(GREEN + BOLD + "🟢 Entering 'Green Hat' mode..." + ENDC)
    elif hacker_mode == "Medium":
        print(BLUE + BOLD + "🔵 Entering 'Blue Hat' mode..." + ENDC)
    elif hacker_mode == "Hard":
        print(RED + BOLD + "🔴 Entering 'Red Hat' mode..." + ENDC)

    # Game setup
    def generate_code():
        return ''.join(random.sample('0123456789', 4))

    secret_code = generate_code()
    max_attempts = {"Easy": 5, "Medium": 3, "Hard": 2}[hacker_mode]
    confirm_time = 5

    confirmation_received = threading.Event()

    def confirm_countdown(timeout):
        for remaining in range(timeout, 0, -1):
            if confirmation_received.is_set():
                return
            print(
                f"⏳ Confirm within {remaining:02d}s... Press Enter! ",
                end='\r'
            )
            time.sleep(1)

        if not confirmation_received.is_set():
            print("\n⏰ Time's up! You didn't confirm your guess.")

    def wait_for_confirmation():
        input()
        confirmation_received.set()

    def get_feedback(guess, code):
        correct_place = sum(g == c for g, c in zip(guess, code))
        correct_digits = sum(
            min(guess.count(d), code.count(d))
            for d in set(guess)
        )
        return correct_place, correct_digits - correct_place

    # Game loop
    attempts = 0
    access_granted = False

    def mission_story(round_number):
        if round_number % 2 == 0:
            return (
                GREEN + BOLD + "🛟 GOOD PATH" + ENDC,
                "A fake government server is about to trigger a toxin lockout. "
                "Crack the vault and save civilians before the city goes dark."
            )

        return (
            RED + BOLD + "💥 EVIL PATH" + ENDC,
            "A fake bank is hiding stolen funds and private records. "
            "Break the vault, drain the dirty money, and expose the syndicate."
        )

    while attempts < max_attempts:
        print("\n" + "-" * 40)
        story_label, story_text = mission_story(attempts + 1)
        print(story_label)
        print(BLUE + story_text + ENDC)
        print(f"💻 Attempt {attempts + 1}/{max_attempts}")

        guess = input(
            "Enter your 4-digit guess (unique digits): "
        ).strip()

        if (
            len(guess) != 4
            or not guess.isdigit()
            or len(set(guess)) != 4
        ):
            print(
                RED
                + "❌ Invalid guess. Must be 4 unique digits."
                + ENDC
            )
            continue

        print(f"🔐 You entered: {guess}")
        print(
            f"⏱ You have {confirm_time} seconds to confirm "
            "your guess by pressing Enter..."
        )

        confirmation_received.clear()

        countdown_thread = threading.Thread(
            target=confirm_countdown,
            args=(confirm_time,)
        )

        input_thread = threading.Thread(
            target=wait_for_confirmation
        )

        countdown_thread.start()
        input_thread.start()

        countdown_thread.join()

        if confirmation_received.is_set():

            # WIN ONLY IF CODE MATCHES
            if guess == secret_code:
                access_granted = True
                print(
                    GREEN
                    + BOLD
                    + "\n🎉 Access Granted! You've cracked the vault!"
                    + ENDC
                )
                break

            correct_place, correct_digits = get_feedback(
                guess,
                secret_code
            )

            print(
                BLUE
                + f"🧩 {correct_place} digits in correct place, "
                  f"{correct_digits} correct digits in wrong place."
                + ENDC
            )

        else:
            print(
                RED
                + "❌ You failed to confirm in time."
                + ENDC
            )

        attempts += 1

    # Endgame result
    if not access_granted:
        print(
            RED
            + "\n💀 You failed to hack the vault..."
            + ENDC
        )
    else:
        print(
            GREEN
            + f"\n🔓 The vault opened with the code: {secret_code}"
            + ENDC
        )

    input(
        BLUE
        + "\nPress Enter to see your final message..."
        + ENDC
    )

    winning_statements = [
        "🏆 You earned every bit of that win. Fantastic work!",
        "🎯 What an impressive win! Your dedication really shows.",
        "🚀 You've set a new standard for success—well done!",
        "📈 This is just the beginning of even greater achievements!",
        "🧠 See how wonderful it is to use your brain!",
        "🎉 Congratulations on your well-deserved victory!"
    ]

    losing_statements = [
        "💡 Every setback is just a step toward future success. Keep going!",
        "🔁 It's not about winning or losing but about growing and improving.",
        "🛡️ Some of the best champions have faced losses along the way.",
        "📘 This is only a small chapter in your journey.",
        "💪 You're getting stronger every time. Don't stop!",
        "🧱 This challenge is part of your bigger story. Don't give up!"
    ]

    print(
        "\n"
        + random.choice(
            winning_statements
            if access_granted
            else losing_statements
        )
    )


if __name__ == "__main__":
    main()