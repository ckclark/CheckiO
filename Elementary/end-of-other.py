from collections import defaultdict
def checkio(words_set):
    suffices = defaultdict(set)
    for word in words_set:
        suffices[len(word)].add(word)
    return any(w[-i:] in s and len(w) > i for i, s in suffices.iteritems() for w in words_set)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({u"hello", u"lo", u"he"}) == True, "helLO"
    assert checkio({u"hello", u"la", u"hellow", u"cow"}) == False, "hellow la cow"
    assert checkio({u"walk", u"duckwalk"}) == True, "duck to walk"
    assert checkio({u"one"}) == False, "Only One"
    assert checkio({u"helicopter", u"li", u"he"}) == False, "Only end"
