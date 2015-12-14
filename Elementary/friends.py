from collections import defaultdict

class Friends:
    def __init__(self, connections):
        self.adj = defaultdict(set)
        for conn in connections:
            a, b = conn
            self.adj[a].add(b)
            self.adj[b].add(a)

    def add(self, connection):
        a, b = connection
        if b in self.adj[a]:
            return False
        else:
            self.adj[a].add(b)
            self.adj[b].add(a)
            return True

    def remove(self, connection):
        a, b = connection
        if b in self.adj[a]:
            self.adj[a].remove(b)
            self.adj[b].remove(a)
            if not self.adj[a]:
                self.adj.pop(a)
            if not self.adj[b]:
                self.adj.pop(b)
            return True
        else:
            return False

    def names(self):
        return set(self.adj)

    def connected(self, name):
        return self.adj.get(name, set())

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
