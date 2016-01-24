import numpy as np
import sys

def solve(R, C, A, L, V, B, T, r0, c0, Dr, Dc):
    print 'solved'


def columndist(C, c1, c2):
    return min(abs(c1 - c2), C - abs(c1 - c2))


def covered(C, r, c, u, v, V):
    return (r - u) ** 2 + columndist(c, v) ** 2 <= V ** 2


def main(f):
    parse_ints = lambda row: map(int, row.split())

    (R, C, A) = parse_ints(f.next())
    (L, V, B, T) = parse_ints(f.next())

    Dr = np.zeros((A, R, C), np.int32)
    Dc = np.zeros((A, R, C), np.int32)

    r0, c0 = parse_ints(f.next())

    for _ in xrange(L):
        (r, c) = parse_ints(f.next())

    for a in xrange(A):
        for r in xrange(R):
            row = parse_ints(f.next())
            for (dr, dc) in chunks(row, 2):
                Dr[a, r, c] = dr
                Dc[a, r, c] = dc

    solve(R, C, A, L, V, B, T, r0, c0, Dr, Dc)


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i+n]


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        main(f)
