def letter_queue(commands):
    q = [None] * 30
    head = tail = 0
    for cmd in commands:
        arg = cmd.split()
        if arg[0] == 'PUSH':
            q[head] = arg[1]
            head += 1
        elif arg[0] == 'POP':
            if tail < head:
                tail += 1
    return ''.join(q[tail:head])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
