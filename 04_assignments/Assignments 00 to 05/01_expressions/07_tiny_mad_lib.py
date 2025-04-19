SENTENCE_START: str = "GIAIC is fun To Learn AI. I learned to program and used Python to make my "  # adjective noun verb

def main():
    # Get the three inputs from the user to make the adlib
    adjective: str = input("Please type an adjective and press enter: ")
    noun: str = input("Please type a noun and press enter: ")
    verb: str = input("Please type a verb and press enter: ")

    # Create the sentence by concatenating the user inputs with the sentence starter
    sentence = SENTENCE_START + adjective + " " + noun + " " + verb + "!"
    
    # Print the final sentence
    print(sentence)

# Main entry point
if __name__ == '__main__':
    main()
