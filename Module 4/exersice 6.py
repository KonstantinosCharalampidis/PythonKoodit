import random
n = int(input("How many random points: "))
circle = 0
for _ in range(n):
    x= random.uniform(-1,1)
    y= random.uniform(-1,1)
    if x**2 + y**2 <=1:
        circle +=1
pi= 4 *circle/n
print("Approximation pi:",pi)