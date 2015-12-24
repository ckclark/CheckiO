def checkio(marbles, step):
    l = len(marbles)
    white = marbles.count('w')
    prob = [float(white), float(l - white)]
    for i in xrange(step - 1):
        prob = [prob[0] / l * (prob[0] - 1) + prob[1] / l * (prob[0] + 1), prob[1] / l * (prob[1] - 1) + prob[0] / l * (prob[1] + 1)]
    return round(prob[0] / l, 2)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u'bbw', 3) == 0.48, "1st example"
    assert checkio(u'wwb', 3) == 0.52, "2nd example"
    assert checkio(u'www', 3) == 0.56, "3rd example"
    assert checkio(u'bbbb', 1) == 0, "4th example"
    assert checkio(u'wwbb', 4) == 0.5, "5th example"
    assert checkio(u'bwbwbwb', 5) == 0.48, "6th example"
