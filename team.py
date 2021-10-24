import math
import matplotlib.pyplot as plt
l = []#x-axis
m = []#y-axis
cnt = 0
r = int(input())
for i in range(-r,r+1):
    for j in range(-r,r+1):
        if (i**2) + (j**2) == r:
            cnt = cnt + 1
            print(f"({i},{j})")
            l.append(i)
            m.append(j)
'''
print(f"(0,{r})")
l.append(0)
m.append(r)
print(f"(0,{-r})")
l.append(0)
m.append(-r)
print(f"({r},{0})")
l.append(r)
m.append(0)
print(f"({-r},{0})")
l.append(-r)
m.append(0)
'''


print(f"Radius = {r}")
print(f"Circumfrence = {2*math.pi*r}")
print(f"Area = {math.pi*(r**2)}")
print(f"Number of points = {cnt}")
print(l)
print(m)


for i in range(len(l)):
        plt.plot(l[i],m[i],"bo")
plt.show()

