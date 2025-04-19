import random

PROMPT: str = "What do you want? "

JOKES: list = [
    "Here's a joke for you! Why do programmers prefer dark mode? Because light attracts bugs!",
    "Here's a joke for you! How many programmers does it take to change a light bulb? None – it's a hardware problem.",
    "Here's a joke for you! A programmer's wife tells him: 'Go to the store and buy a loaf of bread. If they have eggs, buy a dozen.' He returns with 13 loaves of bread.",
    "Here's a joke for you! Why do Java developers wear glasses? Because they can't C#.",
    "Here's a joke for you! Real programmers count from 0."
]

SORRY: str = "Sorry I only tell jokes."

def main():
    user_input = input(PROMPT).strip().lower()

    if user_input == "joke":
        print(random.choice(JOKES))
    else:
        print(SORRY)

if __name__ == "__main__":
    main()
