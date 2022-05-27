#Finding Anagrams


def find_anagrams(word, anagram):
    val1 = word.replace(" ", "")
    val2 = anagram.replace(" ", "")
    sortWord = sorted(val1)
    sortAnagram = sorted(val2)
    len_word = len(sortWord)
    len_anagram = len(sortAnagram)
    if len_anagram != len_word:
        result = False
    else:
        for i in range(0,len_word):
            if sortWord[i] == sortAnagram[i]:
                check = True
            else:
                check = False
            if check == False:
                result = False
            else:
                result = True

    return result
