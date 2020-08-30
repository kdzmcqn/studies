# arr = [1, 5, 3 , 3, 5, 3, 6]
# print(arr.count(3))
# print(arr.index(5))
#
# query = [[1,1],[1,2]]
# for k,v in query:
#     if k == 2:
#         print(k," - ",v)

queries = [[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]

# def freqQuery(queries):
#     arr = []
#     ans = []
#     stop = False
#     for k, v in queries:
#         if k == 1:
#             arr.append(v)
#         elif k == 2:
#             if (v in arr) and (arr.count(v) > 1):
#                 arr.pop(arr.index(v))
#         elif k == 3:
#             for i in arr:
#                 print(arr.count(i), '>', v, ' ?')
#                 if arr.count(i) >= v:
#                     ans.append(1)
#                     stop = True
#                     break
#             if not stop:
#                 ans.append(0)
#     print(ans)
#     return ans

from collections import Counter,defaultdict

def freqQuery(queries):
    c = Counter()
    d = defaultdict(set)
    for x, y in queries:
        v = c[y]
        if x == 1:
            d[v].discard(y)
            d[v + 1].add(y)
            c[y] = v + 1
        elif x == 3:
            yield 1 if d[y] else 0
        elif v:
            d[v].discard(y)
            d[v - 1].add(y)
            c[y] = v - 1

print(*freqQuery(queries))



