from data import LETTERS, NUMBERS
import sys

def GetUserInput() -> str:
    user_input = input("Would you like to convert text to morse code? (Y/n): ")
    if user_input.lower() == "y":
        return ConvertTextList(user_input=input("Enter the text you would like to convert: "))
    elif user_input.lower() == "n":
        input("Press any key to exit the application...")
        sys.exit(0)
    else:
        return "Invalid Input!"

def ConvertTextList(user_input : str) -> list[str]:
    output : list[str] = []
    for _, character in enumerate(user_input):
        try:
            output.append(LETTERS[str.upper(character)])
        except KeyError:
            print(f'The character "{character}" is invalid!')
    print(f"The morse code for each valid character in the sequence provided: ")
    return output

def main() -> None:
    while True:
        print(GetUserInput())

if __name__ == "__main__":
    main()