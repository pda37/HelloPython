def detectCapitalUse(word):
    if word.upper() == word or word.lower() == word:
        return True
    elif word[0].upper() == word[0] and word[1:].lower() == word[1:]:
        return True
    return False


print(detectCapitalUse('Wer'))
