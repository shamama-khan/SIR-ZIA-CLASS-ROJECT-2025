import random 

N_NUMBERS: int = 10 
MIN_VALUE: int = 1  
MAX_VALUE: int = 100  

def main():
    """
    Generate and print 10 random numbers in the range 1 to 100.
    - random.sample() is used to generate a list of unique numbers
    - The range is from MIN_VALUE to MAX_VALUE (inclusive)
    """
    random_numbers = random.sample(range(MIN_VALUE, MAX_VALUE + 1), N_NUMBERS)
    
    print(" ".join(map(str, random_numbers)))

if __name__ == '__main__':
    main()
