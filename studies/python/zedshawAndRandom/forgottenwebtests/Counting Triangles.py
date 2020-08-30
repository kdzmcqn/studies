def CntTri(A):
    A.sort()
    sides_num = len(A)
    tri_count = 0
    for e in range(0, sides_num):
        sa = 0
        sb = e - 1
        while sa < sb:
            if A[e] < A[sb] + A[sa]:
                print(A[e],"<", A[sb],"+", A[sa],"=", A[sb] + A[sa], end=" ")
                print('')
                tri_count += 1
                sb -= 1
            else:
                sa += 1

    return tri_count

n = [1, 2, 3, 4, 5, 7, 8, 9, 10]
print("No. of triangles counted:",CntTri(n))
# [a,b,c,d,e]
# [0,1,2,3,4]
