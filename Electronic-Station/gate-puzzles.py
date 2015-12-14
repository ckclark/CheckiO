from collections import defaultdict
import re

def find_word(message):
    words = filter(None, re.findall(r'[a-z]+', message.lower()))
    l = len(words)
    s = defaultdict(float)
    for i in xrange(l):
        for j in xrange(i):
            w1, w2 = words[i], words[j]
            like = 0
            if w1[0] == w2[0]:
                like += .10
            if w1[-1] == w2[-1]:
                like += .10
            if len(w1) < len(w2):
                like += .30 * len(w1) / len(w2)
            else:
                like += .30 * len(w2) / len(w1)
            like += .50 * len(set(w1) & set(w2)) / len(set(w1) | set(w2))
            s[i] += like
            s[j] += like
    ans = l - 1
    for idx in xrange(l - 1, -1, -1):
        if s[idx] > s[ans]:
            ans = idx
    return words[ans]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word(u"Speak friend and enter.") == "friend", "Friend"
    assert find_word(u"Beard and Bread") == "bread", "Bread is Beard"
    assert find_word(u"The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     u"I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word(u"Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     u" According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word(u"One, two, two, three, three, three.") == "three", "Repeating"
