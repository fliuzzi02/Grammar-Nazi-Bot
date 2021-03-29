from spellchecker import SpellChecker
from autocorrect import Speller

spell = SpellChecker()

def fun(phrase, lang):
    t = Speller(lang)
    print(phrase)
    words = spell.split_words(phrase)
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