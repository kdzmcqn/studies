"""
1
2
3
4 
5
1,2
2,3
3,4
4,5
1,2,3
2,3,4
3,4,5
1,2,3,4
2,3,4,5
1,2,3,4,5
"""


def kadane(A, m):
    b = []
    max_current = max_global = A[0]
    for i in range(1, len(A)-1):
        max_current = max(A[i], max_current + A[i])
        max_global = max(max_global, max_current)
        b.append(max_current)

    c = []
    for i in b:
        c.append(i % m)

    return max_global, max(c), c, b


modulo = 8
a = [2,3,4,5]
print(kadane(a, modulo))

# d = 5 % 3
# e = 2 % 3
# f = 3 % 100
# print(d, e, f)


for _ in range(int(input())):
    N, M = map(int, input().split())
    A = [int(a) for a in input().split()]

    # precompute sum(A[:j]) for 0 <= j <= N
    b = 0
    B = [b]
    for a in A:
        b = (a + b) % M
        B.append(b)

    order = sorted(range(len(B)), key=lambda i: B[i])  # sort indices
    best = 0
    lenB = len(B)
    for a, j in enumerate(order):
        if j == 0:
            continue
        a = (a + 1) % lenB
        i = order[a]
        Bj = B[j]
        ii = 0
        while i >= j or B[i] == Bj:
            a = (a + 1) % lenB
            i = order[a]
            ii += 1
            if ii > 100:  # hack
                break
        this = (Bj - B[i]) % M
        if this > best:
            best = this
    print(best)



# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the maximumSum function below.
def maximumSum(A, M):
    b = 0
    B = [b]
    for a in A:
        b = (a + b) % M
        B.append(b)

    order = sorted(range(len(B)), key=lambda i: B[i])  # sort indices
    best = 0
    lenB = len(B)
    for a, j in enumerate(order):
        if j == 0:
            continue
        a = (a + 1) % lenB
        i = order[a]
        Bj = B[j]
        ii = 0
        while i >= j or B[i] == Bj:
            a = (a + 1) % lenB
            i = order[a]
            ii += 1
            if ii > 100:  # hack
                break
        this = (Bj - B[i]) % M
        if this > best:
            best = this
    return best


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()

from bisect import bisect_right

T = int(input())

for _ in range(T):
    N, M = [int(x) for x in input().split()]
    s = 0
    maxm = 0
    acc = [0]

    for i, x in enumerate(map(int, input().split())):
        s += x
        s %= M
        idx = bisect_right(acc, s)
        if idx > i:
            maxm = max(maxm, s)
        else:
            maxm = max(maxm, M + s - acc[idx])
        acc.insert(idx, s)

    print(maxm)