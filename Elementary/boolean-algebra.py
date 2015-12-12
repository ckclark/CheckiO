from operator import xor, and_, or_, eq
OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")
opmap = dict(zip(OPERATION_NAMES, (and_, or_, lambda x,y:(not x) or y, xor, eq)))

def boolean(x, y, operation):
    return opmap[operation](x, y)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, u"conjunction") == 0, "and"
    assert boolean(1, 0, u"disjunction") == 1, "or"
    assert boolean(1, 1, u"implication") == 1, "material"
    assert boolean(0, 1, u"exclusive") == 1, "xor"
    assert boolean(0, 1, u"equivalence") == 0, "same?"
