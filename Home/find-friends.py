def find_root(parent, n):
    if parent[n] != n:
        parent[n] = find_root(parent, parent[n])
    return parent[n]

def check_connection(network, first, second):
    parent = dict()
    for conn in network:
        a, b = conn.split('-')
        parent.setdefault(a, a)
        parent.setdefault(b, b)
        ra = find_root(parent, a)
        rb = find_root(parent, b)
        parent[ra] = rb

    return find_root(parent, first) == find_root(parent, second)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
