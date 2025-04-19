def main():
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total_cost = 0

    for fruit_name, price in fruits.items():
        while True:
            try:
                amount_bought = int(input(f"How many ({fruit_name}) do you want?: ").strip())
                if amount_bought < 0:
                    print("Please enter a non-negative number.")
                    continue
                total_cost += price * amount_bought
                break
            except ValueError:
                print("Please enter a valid number.")

    print(f"\nYour total is ${total_cost:.2f}")

if __name__ == '__main__':
    main()
