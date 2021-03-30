from autocorrect import Speller

def fun(phrase, lang):
    t = Speller(lang)
    print(phrase)
    words = phrase.split()
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