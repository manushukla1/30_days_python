def is_anagram(s1, s2):

    check_dict ={}
    # Your code here!
    if len(s1) != len(s2):
        return False
    for char in s1:
        if char in s2:

        return False
    else:
     return True


First_word = input("Enter first word: ").lower()
Second_word = input("Enter second word: ").lower()

Anagram_Check = is_anagram(First_word, Second_word)
print(Anagram_Check)


