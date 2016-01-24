import numpy as np
import random
import sys
from collections import defaultdict


def score(R, C, T, B, V, Dr, Dc, alt, r0, c0, targets):
    print alt

    covered_turn = defaultdict(set)
    score = 0
    for b in xrange(B):
        r = r0
        c = c0
        for t in xrange(T):
            a = alt[b, t]
            dr = Dr[a, r, c]
            dc = Dc[a, r, c]
            r += dr
            c += dc
            c %= C
            if not (1 <= r <= R-1):
                break
            for tr, tc in targets:
                if covered(C, r, c, tr, tc, V):
                    if not (tr, tc) in covered_turn[t]:
                        score += 1
                        covered_turn[t].add((tr, tc))
        print 'loon', b, score
    print score


def da(alt, A):
    if alt <= 1:
        return random.choice([0, 1])
    if 1 < alt < A:
        return random.choice([-1, 0, 1])
    else:
        return random.choice([-1, 0])


def solve(R, C, A, L, V, B, T, r0, c0, Dr, Dc, targets):
    alt = np.zeros((B, T), np.int32)
    dalt = np.zeros((B, T), np.int8)

    # start on alt 1
    for b in xrange(B):
        alt[b, 0] = 1
        dalt[b, 0] = 1

    for t in xrange(T):
        for b in xrange(B):
            dalt[b, t] = da(alt[b, t-1], A)
            alt[b, t] = alt[b, t-1] + dalt[b, t]
    return score(R, C, T, B, V, Dr, Dc, alt, r0, c0, targets)


def columndist(C, c1, c2):
    return min(abs(c1 - c2), C - abs(c1 - c2))


def covered(C, r, c, u, v, V):
    return (r - u) ** 2 + columndist(C, c, v) ** 2 <= V ** 2


def main(f):
    parse_ints = lambda row: map(int, row.split())

    (R, C, A) = parse_ints(f.next())
    (L, V, B, T) = parse_ints(f.next())

    Dr = np.zeros((A+1, R, C), np.int32)
    Dc = np.zeros((A+1, R, C), np.int32)

    r0, c0 = parse_ints(f.next())

    targets = set()
    for _ in xrange(L):
        (r, c) = parse_ints(f.next())
        targets.add((r, c))

    for a in xrange(A):
        for r in xrange(R):
            row = parse_ints(f.next())
            for c, (dr, dc) in enumerate(chunks(row, 2)):
                if a == 0:
                    Dr[a, r, c] = r
                    Dc[a, r, c] = c
                else:
                    Dr[a, r, c] = dr
                    Dc[a, r, c] = dc

    solve(R, C, A, L, V, B, T, r0, c0, Dr, Dc, targets)


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i+n]


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        main(f)
