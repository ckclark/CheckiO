VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
import re

def checkio(text):
    words = filter(lambda x:len(x) > 1 and x.isalpha(), re.split(r'\W', text.upper()))
    ans = 0
    for w in words:
        if all(c in VOWELS for c in w[::2]) and all(c in CONSONANTS for c in w[1::2]):
            ans += 1
        elif all(c in VOWELS for c in w[1::2]) and all(c in CONSONANTS for c in w[::2]):
            ans += 1
    return ans

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
