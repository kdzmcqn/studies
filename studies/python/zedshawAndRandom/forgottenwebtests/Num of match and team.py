def calcNumTeam(mat):
    A = 1
    B = -1
    C = -2 * mat
    x_pos = (-B + (B ** 2 - 4 * A * C) ** 0.5) / (2 * A)
    x_neg = (-B - (B ** 2 - 4 * A * C) ** 0.5) / (2 * A)
    x1i = x_pos - round(x_pos)
    x2i = x_neg - round(x_neg)
    if x_pos > 0 and x1i == 0:
        return x_pos
    else:
        print("Invalid number of matches can be played by two different teams at at time")
    if x_neg > 0 and x2i == 0:
        return x_neg


# C(n,2) = n(n-1)/2
# n^2 - n - 2*(no. of C(n,2))

n = int(input("Input number of teams will play: "))
matches0 = n * (n - 1) / 2
print("Number of matches can be played by", n,"teams:", matches0)

matches = int(input("Input no. of matches to find the no. of teams played. "))
print("Number of team/s:", calcNumTeam(matches))

