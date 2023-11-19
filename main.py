from data import LETTERS, NUMBERS

def ConvertTextList(input : str) -> list[str]:
    output : list[str] = []
    for _, character in enumerate(input):
        try:
            output.append(LETTERS[str.upper(character)])
        except KeyError:
            print(f'The character "{character}" is invalid!')
    print(f"The morse code for each valid character in the sequence provided: ")
    return output

def main() -> None:
    pass

if __name__ == "__main__":
    main()