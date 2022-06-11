t = [1, 4, 2, 5]
x = [2, 3, 4, 1, 4, 5]

def div_point(l):
    for i in range(len(l)):
        if sum(l[0:i]) == sum(l[i+1:]):
            return l[i]

print(div_point(t))