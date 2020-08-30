# N = 101010001
# def solution(N):
#     cnt = 0
#     result = 0
#     found_one = False
#     i = N
#     while i:
#         if i & 1 == 1:
#             if(found_one == False):
#                 found_one = True
#             else:
#                 result = max(result , cnt)
#                 cnt = 0
#         else:
#             cnt += 1
#         i >>= 1
#     return result
# print(solution(N))

N = 1000100001
def bingap(N):
    return len(max(format(N, 'b').strip('0').split('1')))
print(bingap(N))