names=[]
for i in range(5):
    cities=input(f"Enter the name of the city {i+1}: ")
    names.append(cities)
print("These are the cities")
for cities in names:
    print(cities)