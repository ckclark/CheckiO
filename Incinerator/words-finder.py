def checkio(text, words):
    intervals = []
    lowertext = text.lower()
    for word in words.lower().split():
        offset = 0
        while True:
            idx = lowertext.find(word, offset)
            if idx == -1:
                break
            intervals.append((idx, idx + len(word)))
            offset = idx + 1
    intervals.sort()
    merged = []
    for itv in intervals:
        if not merged:
            merged.append(itv)
        else:
            if itv[0] < merged[-1][1]:
                merged[-1] = (merged[-1][0], max(itv[1], merged[-1][1]))
            else:
                merged.append(itv)
    prev = (0, 0)
    ans = []
    for itv in merged:
        ans.append(text[prev[1]:itv[0]])
        ans.append('<span>')
        ans.append(text[itv[0]:itv[1]])
        ans.append('</span>')
        prev = itv
    ans.append(text[prev[1]:])

    return ''.join(ans)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(u"This is only a text example for task example.", u"example") ==
            "This is only a text <span>example</span> for task <span>example</span>."), "Simple test"

    assert (checkio(u"Python is a widely used high-level programming language.", u"pyThoN") ==
            "<span>Python</span> is a widely used high-level programming language."), "Ignore letters cases, but keep original"

    assert (checkio(u"It is experiment for control groups with similar distributions.", u"is im") ==
            "It <span>is</span> exper<span>im</span>ent for control groups with s<span>im</span>ilar d<span>is</span>tributions."), "Several subwords"

    assert (checkio(u"The National Aeronautics and Space Administration (NASA).", u"nasa  THE") ==
            "<span>The</span> National Aeronautics and Space Administration (<span>NASA</span>)."), "two spaces"

    assert (checkio(u"Did you find anything?", "word space tree") ==
            "Did you find anything?"), "No comments"

    assert (checkio(u"Hello World! Or LOL", u"hell world or lo") ==
            "<span>Hello</span> <span>World</span>! <span>Or</span> <span>LO</span>L"), "Contain or intersect"
