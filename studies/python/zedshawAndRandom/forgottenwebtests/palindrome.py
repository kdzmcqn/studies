s = str(input(""))
def reverse(s):
    return s[::-1]
print(reverse(s))
a = reverse(s)
print(s,"is equal to", f"{a}", "?", a == s)


def ispal(bb):
    rev = ''.join(reversed(bb))
    if (bb == rev):
        return True
    return False

print("Input a string to bb")
bb = str(input())
ans = ispal(bb)
if (ans):
    print("Yes")
else:
    print("No")