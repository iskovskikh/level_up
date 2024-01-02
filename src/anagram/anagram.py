

def is_anagram(word1: str, word2: str) -> bool:
    # return sorted(word1) == sorted(word2)

    word1_dict = dict()
    for char_item in word1:
        if char_item in word1_dict:
            word1_dict[char_item] += 1
        else:
            word1_dict[char_item] = 1

    word2_dict = dict()
    for char_item in word2:
        if char_item in word2_dict:
            word2_dict[char_item] += 1
        else:
            word2_dict[char_item] = 1

    return word1_dict == word2_dict
