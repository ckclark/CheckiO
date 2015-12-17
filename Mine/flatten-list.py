# first solution
import itertools as i;flat_list=f=lambda n:int==type(n)and[n]or list(i.chain(*map(f,n)))

# second solution
flat_list=f=lambda n:int==type(n)and[n]or sum(map(f,n),[])

# shortest solution on http://www.checkio.org/mission/flatten-list/publications/veky/python-3/could-be-shorter/
flat_list=f=lambda d:0*d==0 and[d]or sum(map(f,d),[])#)][,)d,f(pam(mus ro]d[dna 0==d*0:d adbmal=f=tsil_talf
#Tweet? Palindrome? Solution.

# try-catch, creative
def flat_list(d):
    try:
        return [int(d)]
    except:
        return sum(map(flat_list, d), [])

if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3]
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1]
