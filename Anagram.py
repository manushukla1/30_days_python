from tabnanny import check


def is_anagram(s1, s2):

    if len(s1) != len(s2):
        return False

    check_dict = {}

    for char in s1:
        if char in check_dict:
            check_dict[char] += 1
        else:
            check_dict[char] = 1

    for char in s2:
        if char in check_dict:
            check_dict[char] -= 1
        else:
            return False

    for values in check_dict.values():
        if values != 0:
            return False

    return True

First_word = input("Enter first word: ").lower()
Second_word = input("Enter second word: ").lower()

Anagram_Check = is_anagram(First_word, Second_word)
print(Anagram_Check)



