from morseTranslate import morse_code


def get_input():
    return input('Enter the text you would like to convert to morse code: ')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    to_translate = get_input().lower()
    translated_list = []
    for char in to_translate:
        translated_list.append(morse_code[char])
    translated = " ".join(translated_list)
    print(f"Morse Code: {translated}")

