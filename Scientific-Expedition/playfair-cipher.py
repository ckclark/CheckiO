from string import lowercase, digits
def build_table(key):
    visited = set()
    table = []
    for c in key:
        if c not in visited:
            visited.add(c)
            table.append(c)
    for c in lowercase + digits:
        if c not in visited:
            table.append(c)
    table = [table[i:i + 6] for i in xrange(0, 36, 6)]
    revtable = dict()
    for i in xrange(6):
        for j in xrange(6):
            revtable[table[i][j]] = i, j
    return table, revtable

def do_code(msg, key, typ):
    table, revtable = build_table(key)
    msg = filter(lambda x:x.isalnum(), msg.lower())
    pairs = []
    i = 0
    while i < len(msg):
        if i == len(msg) - 1:
            if msg[i] == 'z':
                pairs.append('zx')
            else:
                pairs.append(msg[i] + 'z')
            i += 1
        elif msg[i] == msg[i + 1]:
            if msg[i] == 'x':
                pairs.append('xz')
            else:
                pairs.append(msg[i] + 'x')
            i += 1
        else:
            pairs.append(msg[i] + msg[i + 1])
            i += 2

    coded = []
    for pair in pairs:
        p1 = revtable[pair[0]]
        p2 = revtable[pair[1]]
        if p1[0] != p2[0] and p1[1] != p2[1]:
            coded.append(table[p1[0]][p2[1]])
            coded.append(table[p2[0]][p1[1]])
        elif p1[0] == p2[0]:
            d = 6 - (typ + 6) % 6
            coded.append(table[p1[0]][p1[1] - d])
            coded.append(table[p2[0]][p2[1] - d])
        elif p1[1] == p2[1]:
            d = 6 - (typ + 6) % 6
            coded.append(table[p1[0] - d][p1[1]])
            coded.append(table[p2[0] - d][p2[1]])
    return ''.join(coded)

def encode(message, key):
    return do_code(message, key, 1)

def decode(secret_message, key):
    return do_code(secret_message, key, -1)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert encode("Fizz Buzz is x89 XX.", "checkio101") == 'do2y7mt22kry94y2y2', "Encode fizz buzz"
    assert decode("do2y7mt22kry94y2y2", "checkio101") == 'fizxzbuzzisx89xzxz', "Decode fizz buzz"
    assert encode("How are you?", "hello") == 'ea2imb1ht0', "Encode How are you"
    assert decode("ea2imb1ht0", "hello") == 'howareyouz', "Decode How are you"
    assert encode("My name is Alex!!!", "alexander") == 'i1dlkxjqlexn', "Encode Alex"
    assert decode("i1dlkxjqlexn", "alexander") == 'mynameisalex', "Decode Alex"
    assert encode("Who are you?", "human") == 'rnvftc1jd5', "Encode WHo"
    assert decode("rnvftc1jd5", "human") == 'whoareyouz', "Decode Who"
    assert encode("ATTACK AT DAWN", "general") == 'ewwektewhnua', "Encode attack"
    assert decode("ewwektewhnua", "general") == 'attackatdawn', "Decode attack"
