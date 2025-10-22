def sort_wordsAlphatically():
    user_input = input("Enter any String to Arrange in Alphabetical order . ")
    words = user_input.lower().split()
    words.sort()
    print("Words in alphabetical orer : ")
    for word in words:
        print(word)


def sort_words(words):
    return ' '.join(sorted(words.split(), key=str.casefold))


# commands used in solution video for reference
if __name__ == '__main__':
    print(sort_words('banana ORANGE apple'))  # apple banana ORANGE
    sort_wordsAlphatically()
