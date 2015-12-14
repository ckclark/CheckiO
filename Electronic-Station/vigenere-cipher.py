from string import uppercase
from itertools import cycle

def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
    key = []
    if len(new_encrypted) <= len(old_encrypted):
        for i in xrange(len(new_encrypted)):
            key.append((ord(old_encrypted[i]) - ord(old_decrypted[i]) + 26) % 26)
    else:
        for i in xrange(len(old_encrypted)):
            key.append((ord(old_encrypted[i]) - ord(old_decrypted[i]) + 26) % 26)
        for l in xrange(1, (len(key) / 2) + 1):
            for j in xrange(l):
                if len(set(key[j::l])) != 1:
                    break
            else:
                break
        key = key[:l]

    ans = []
    for c, offset in zip(new_encrypted, cycle(key)):
        ans.append(uppercase[ord(c) - ord('A') - offset])
    return ''.join(ans)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert decode_vigenere(u'DONTWORRYBEHAPPY',
                           u'FVRVGWFTFFGRIDRF',
                           u'DLLCZXMFVRVGWFTF') == "BEHAPPYDONTWORRY", "CHECKIO"
    assert decode_vigenere(u'HELLO', u'OIWWC', u'ICP') == "BYE", "HELLO"
    assert decode_vigenere(u'LOREMIPSUM',
                           u'OCCSDQJEXA',
                           u'OCCSDQJEXA') == "LOREMIPSUM", "DOLORIUM"
