COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

def cowsay(text):
    lines = []
    l = 0
    text2 = []
    first = True

    if text.startswith(' '):
        leading = ' '
    else:
        leading = ''

    if text.endswith(' '):
        trailing = ' '
    else:
        trailing = ''

    for w in text.split():
        if first:
            first = False
            w = leading + w
        if len(w) > 39:
            if w.startswith(' '):
                text2.append(' ')
                w = w[1:]
            text2.extend(w[i:i+39] for i in xrange(0, len(w), 39))
        else:
            text2.append(w)
    text2[-1] += trailing

    first = True
    for word in text2:
        if first or l + len(word) + 1 > 39:
            first = False
            cur = [word]
            lines.append(cur)
            l = len(word)
        else:
            l += len(word) + 1
            cur.append(' ' + word)
    lines = map(''.join, lines)
    maxl = len(max(lines, key=len))
    answer = ['\n']
    answer.append(' ')
    answer.append('_')
    answer.append('_' * maxl)
    answer.append('_\n')

    for i, line in enumerate(lines):
        if i == 0 == len(lines) - 1:
            answer.append('< ')
        elif i == 0:
            answer.append('/ ')
        elif i == len(lines) - 1:
            answer.append(r'\ ')
        else:
            answer.append('| ')

        answer.append('{0:{width}}'.format(line, width=maxl))

        if i == 0 == len(lines) - 1:
            answer.append(' >')
        elif i == 0:
            answer.append(' \\')
        elif i == len(lines) - 1:
            answer.append(' /')
        else:
            answer.append(' |')
        answer.append('\n')
    answer.append(' ')
    answer.append('-')
    answer.append('-' * maxl)
    answer.append('-')
    answer.append(COW)

    return ''.join(answer)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    expected_cowsay_two_lines = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    expected_cowsay_many_lines = r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    cowsay_one_line = cowsay('Checkio rulezz')
    assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % cowsay_one_line

    cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
    assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s' % cowsay_two_lines

    cowsay_many_lines = cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
                                'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
    assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n%s' % cowsay_many_lines
