def checkio(data):

    lower, upper, digit = False, False, False
    for c in data:
        if 'a' <= c <= 'z':
            lower = True
        elif 'A' <= c <= 'Z':
            upper = True
        elif '0' <= c <= '9':
            digit = True
        else:
            return False
    return len(data) >= 10 and lower and upper and digit

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example"
