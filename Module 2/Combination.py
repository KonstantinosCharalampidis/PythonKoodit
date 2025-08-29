import random
comb = input("Choose combination code: ")

if comb == "three digit":
    a = random.randint(0,9)
    b = random.randint(0,9)
    c = random.randint(0,9)
    print("The three digit code is:", (a,b,c))

else:
    d = random.randint(1,6)
    e = random.randint(1,6)
    f = random.randint(1,6)
    g = random.randint(1,6)
    print("The four digit combination code is:", (d,e,f,g))



