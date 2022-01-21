import math


def formula_calculator(D):
    C = 50
    H = 30

    Q = math.sqrt((2*C*D)/H)
    return Q


I = input()
print(I)
res = []
for x in I.split(','):
    print(x)
    res.append(int(formula_calculator(int(x))))

print(res)
