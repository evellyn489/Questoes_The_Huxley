sentence = input()

letters = {}

for character in sentence:
    if character in letters:
        letters[character] = int(letters[character]) + 1
    else:
        letters[character] = 1

for elemento in sorted(letters.keys(), reverse=True):
    print(f'{elemento} {letters[elemento]}')
