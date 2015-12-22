exec 'checkio=lambda n: all(n' + chr(ord(',') ^ ord('\t')) + 'i for i in r' + 'ange(' + chr(ord('\t') + ord(')')) + ',n))'
assert checkio(5) == True
assert checkio(18) == False
