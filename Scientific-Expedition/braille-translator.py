def convert(code):
    bin_code = bin(code)[2:].zfill(6)[::-1]
    return [[int(bin_code[j + i * 3]) for i in range(2)] for j in range(3)]


LETTERS_NUMBERS = list(map(convert,
                           [1, 3, 9, 25, 17, 11, 27, 19, 10, 26,
                            5, 7, 13, 29, 21, 15, 31, 23, 14, 30,
                            37, 39, 62, 45, 61, 53, 47, 63, 55, 46, 26]))
CAPITAL_FORMAT = convert(32)
NUMBER_FORMAT = convert(60)
PUNCTUATION = {",": convert(2), "-": convert(18), "?": convert(38),
               "!": convert(22), ".": convert(50), "_": convert(36)}
WHITESPACE = convert(0)


def braille_page(text):
    codes = []
    for c in text:
        if c.isupper():
            codes.append(CAPITAL_FORMAT)
            codes.append(LETTERS_NUMBERS[ord(c) - ord('A')])
        elif c.islower():
            codes.append(LETTERS_NUMBERS[ord(c) - ord('a')])
        elif c.isdigit():
            codes.append(NUMBER_FORMAT)
            codes.append(LETTERS_NUMBERS[(ord(c) - ord('0') + 9) % 10])
        elif c in PUNCTUATION:
            codes.append(PUNCTUATION[c])
        else: # space
            codes.append(WHITESPACE)
    charwidth = min(10, len(codes))
    charheight = (len(codes) - 1) / charwidth + 1
    output = [[0] * (charwidth * 3 - 1) for _ in xrange(charheight * 4 - 1)]

    for i, code in enumerate(codes):
        px, py = (i / charwidth) * 4, (i % charwidth) * 3
        for x in xrange(3):
            for y in xrange(2):
                output[px + x][py + y] = code[x][y]
    return output


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def checker(func, text, answer):
        result = func(text)
        return answer == tuple(tuple(row) for row in result)

    assert checker(braille_page, u"hello 1st World!", (
        (1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1),
        (1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1),
        (0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0))
    ), "Example"
    assert checker(braille_page, u"42", (
        (0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0),
        (0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0),
        (1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0))), "42"
    assert checker(braille_page, u"CODE", (
        (0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1),
        (0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0))
    ), "CODE"
