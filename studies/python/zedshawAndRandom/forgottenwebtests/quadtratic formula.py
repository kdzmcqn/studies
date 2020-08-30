#  A x^2 + B x + C

A = 1
B = -1
C = -2*15

# C(n,2) = n(n-1)/2
# n^2 - n - 2*(no. of C(n,2))

x_pos = (-B + (B**2 - 4*A*C)**0.5)/(2*A)
x_neg = (-B - (B**2 - 4*A*C)**0.5)/(2*A)

#number of teams n
n = 6
matches = n*(n - 1)/2
print("Number of matches:", matches)

print("x1 =",x_pos, "; x2 =",x_neg)

if (x_pos > 0):
    print("There are", x_pos,"number of teams.")
if (x_neg > 0):
    print("There are", x_neg,"number of teams.")