from data import LETTERS, NUMBERS
import sys

def GetUserInput() -> list[str]:
    """
    Get user input to determine whether to convert text to Morse code or exit the application.

    Returns:
        str: If 'Y' is entered, it returns the Morse code for the entered text.
             If 'n' is entered, it exits the application.
             If an invalid input is given, it returns 'Invalid Input!'.
    """
    
    user_input = input("Would you like to convert text to morse code? (Y/n): ")
    if user_input.lower() == "y":
        return ConvertTextList(user_input=input("Enter the text you would like to convert: "))
    elif user_input.lower() == "n":
        input("Press any key to exit the application...")
        sys.exit(0)
    else:
        return ["Invalid Input!"]

def ConvertTextList(user_input : str) -> list[str]:
    """
    Convert a string of text to a list of Morse code representations for each valid character.

    Args:
        user_input (str): The input text to be converted.

    Returns:
        list[str]: A list containing the Morse code representation for each valid character.
    """
    
    output : list[str] = []
    for _, character in enumerate(user_input):
        if character.isalpha():
            output.append(LETTERS[str.upper(character)])
        elif character.isnumeric():
            output.append(NUMBERS[character])
    print(f"The morse code for each valid character in the sequence provided: ")
    return output

def main() -> None:
    """
    Main function to run the Morse code conversion application.

    This function runs a continuous loop, prompting the user for input and
    displaying the resulting Morse code. It utilizes the GetUserInput and
    ConvertTextList functions to handle user interactions and text conversion.

    Note:
        The loop continues until the user chooses to exit the application.

    Raises:
        SystemExit: Exits the application if the user chooses to do so.

    Returns:
        None
    """
    
    while True:
        print(GetUserInput())

if __name__ == "__main__":
    main()