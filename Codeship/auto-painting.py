def checkio(capacity, number):
    if number <= capacity:
        s = ''.join(map(str, xrange(number)))
        return ','.join([s, s])
    else:
        start = 0
        ans = []
        for i in xrange(number * 2 / capacity):
            ans.append(''.join(map(str, [(start + j) % number for j in xrange(capacity)])))
            start = (start + capacity) % number
        rem = (number * 2) % capacity
        if rem > 0:
            ans.append(''.join(map(str, [(start + j) % number for j in xrange(rem)])))
        return ','.join(ans)

if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    def check_solution(func, k, n, max_steps):
        result = func(k, n)
        actions = result.split(",")
        if len(actions) > max_steps:
            print("It can be shorter.")
            return False
        details = [0] * n
        for act in actions:
            if len(act) > k:
                print("The system can contain {0} detail(s).".format(k))
                return False
            if len(set(act)) < len(act):
                print("You can not place one detail twice in one load")
                return False
            for ch in act:
                details[int(ch)] += 1
        if any(d < 2 for d in details):
            print("I see no painted details.")
            return False
        if any(d > 2 for d in details):
            print("I see over painted details.")
            return False
        return True

    assert check_solution(checkio, 2, 3, 3), "1st Example"
    assert check_solution(checkio, 6, 3, 2), "2nd Example"
    assert check_solution(checkio, 3, 6, 4), "3rd Example"
    assert check_solution(checkio, 1, 4, 8), "4th Example"
    assert check_solution(checkio, 2, 5, 5), "5th Example"
