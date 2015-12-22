VOWELS = "aeiouy"

def translate(phrase):
    ans = []
    it = iter(phrase)
    while True:
        try:
            c = it.next()
            ans.append(c)
            if c in VOWELS:
                it.next()
                it.next()
            elif c.isalpha():
                it.next()
        except StopIteration:
            break

    return ''.join(ans)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate(u"hieeelalaooo") == "hello", "Hi!"
    assert translate(u"hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate(u"aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate(u"sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
