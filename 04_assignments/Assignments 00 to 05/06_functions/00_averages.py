def average(a: float, b: float) -> float:
    """
    Returns the number which is halfway between a and b.
    """
    total = a + b
    return total / 2

def main():
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    
    final_avg = average(avg_1, avg_2)
    print("Average of 0 and 10:", avg_1)
    print("Average of 8 and 10:", avg_2)
    print("Final average:", final_avg)

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
