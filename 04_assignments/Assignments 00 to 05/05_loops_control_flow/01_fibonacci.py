MAX_TERM_VALUE: int = 10000

def generate_fibonacci():
    fib_sequence = [0, 1]  # Initializing the sequence with the first two terms.
    
    while True:
        next_term = fib_sequence[-1] + fib_sequence[-2]  # Sum of the last two terms
        if next_term >= MAX_TERM_VALUE:
            break
        fib_sequence.append(next_term)
    
    return fib_sequence

def main():
    fib_sequence = generate_fibonacci()
    print(" ".join(map(str, fib_sequence)))

if __name__ == '__main__':
    main()
