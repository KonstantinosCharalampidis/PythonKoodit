z = int(input("Length of zander in cm: "))
if z>= 42:
    print("This zander meets the size limit")
else:
    print("This zander doesn't meet the size limit")
    print("It has to be ",(42-z),"cm longer")