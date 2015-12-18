from math import log
def super_root(number):
    L, U = 1e-5, 10
    while U ** U - L ** L > .001:
        mid = (L + U) / 2
        if mid * log(mid) > log(number):
            U = mid
        else:
            L = mid
    return L

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def check_result(function, number):
        result = function(number)
        if not isinstance(result, (int, float)):
            print("The result should be a float or an integer.")
            return False
        p = result ** result
        if number - 0.001 < p < number + 0.001:
            return True
        return False
    assert check_result(super_root, 4), "Square"
    assert check_result(super_root, 9), "Cube"
    assert check_result(super_root, 81), "Eighty one"
