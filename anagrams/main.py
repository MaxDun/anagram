def reverse_word(text):
    first_list = text.split(' ')
    second_list = []

    for word in first_list:
        third_list = []
        for letters in word:
            if letters.isalpha():
                third_list.append(letters)
            third_list.reverse()

        for ind, letters_2 in enumerate(word):
            if not letters_2.isalpha():
                third_list.insert(ind, letters_2)
        second_list.append(''.join(third_list))

    reverse_string = ' '.join(second_list)
    return reverse_string


if __name__ == '__main__':
    print(reverse_word('qqw123we'))
