from autocorrect import Speller

def split(lst):
    return (lst[0].split())


def fun(phrase, lang):
    t = Speller(lang)
    print(phrase)
    words = split(phrase)
    misspelled = []

    for word in words:
        word.lower()
        corrected = t(word)
        if word == corrected:
            print("word is correct")
        else:
            print(word+" = "+corrected)
            misspelled.append(word)

    return misspelled