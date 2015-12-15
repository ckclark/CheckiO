def digit_stack(commands):
    stack = []
    ans = 0
    for cmd in commands:
        args = cmd.split()
        if args[0] == 'PUSH':
            stack.append(int(args[1]))
        elif args[0] == 'POP':
            if stack:
                ans += stack.pop()
        elif args[0] == 'PEEK':
            if stack:
                ans += stack[-1]
    return ans

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
