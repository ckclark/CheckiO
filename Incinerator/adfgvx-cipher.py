from collections import defaultdict
from itertools import cycle, product

def encode(message, secret_alphabet, keyword):
    ADFGVX = 'ADFGVX'
    encrypted1 = ''.join(ADFGVX[secret_alphabet.index(c) / 6] + ADFGVX[secret_alphabet.index(c) % 6] for c in message.lower() if c.isalnum())
    table = defaultdict(list)
    for k, v in zip(cycle(sorted(list(set(keyword)), key=keyword.index)), encrypted1):
        table[k].append(v)
    ret = []
    for k in sorted(table):
        ret.append(''.join(table[k]))
    return ''.join(ret)

def decode(message, secret_alphabet, keyword):
    ADFGVX = 'ADFGVX'
    keyword = sorted(list(set(keyword)), key=keyword.index)
    m = len(message) % len(keyword)

    table = {k: len(message) / len(keyword) + (1 if i < m else 0) for i, k in enumerate(keyword)}

    ptr = 0
    for k in sorted(keyword):
        end = ptr + table[k]
        table[k] = message[ptr:end]
        ptr = end

    encrypted1 = [table[k][i] for (i, k), _ in zip(product(xrange(len(message) / len(keyword) + 1), keyword), xrange(len(message)))]

    ans = []
    for i in xrange(0, len(encrypted1), 2):
        ans.append(secret_alphabet[ADFGVX.index(encrypted1[i]) * 6 + ADFGVX.index(encrypted1[i + 1])])
    return ''.join(ans)

if __name__ == '__main__':
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"
    assert decode("FXGAFVXXAXDDDXGA",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'iamgoing', "decode I am going"
    assert encode("attack at 12:00 am",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"
    assert decode("DGDDDAGDDGAFADDFDADVDVFAADVX",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'attackat1200am', "decode attack"
    assert encode("ditiszeergeheim",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"
    assert decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'ditiszeergeheim', "decode ditiszeergeheim"
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"
    assert decode("DXGAXAAXXVDDFGFX",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'iamgoing', "decode weasel == weasl"
