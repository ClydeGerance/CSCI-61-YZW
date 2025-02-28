# RPG name is Final Fantasy!

ALBHED_TO_ENG = {
    'a': 'e', 'b': 'p', 'c': 's', 'd': 't', 'e': 'i', 'f': 'w', 'g': 'k', 'h': 'n', 'i': 'u', 'j': 'v',
    'k': 'g', 'l': 'c', 'm': 'l', 'n': 'r', 'o': 'y', 'p': 'b', 'q': 'x', 'r': 'h', 's': 'm', 't': 'd',
    'u': 'o', 'v': 'f', 'w': 'z', 'x': 'q', 'y': 'a', 'z': 'j'
}

def al_bhed_to_english(text):

    decoded_text = []
    for char in text:
        if char.lower() in ALBHED_TO_ENG:
            new_char = ALBHED_TO_ENG[char.lower()]
            decoded_text.append(new_char.upper() if char.isupper() else new_char)
        else:
            decoded_text.append(char)
    return ''.join(decoded_text)

al_bhed_text = input("Enter Al Bhed text: ")
decoded_text = al_bhed_to_english(al_bhed_text)

print("Decoded Text: ", decoded_text)
