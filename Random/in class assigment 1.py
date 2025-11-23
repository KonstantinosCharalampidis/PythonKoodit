class Food:
    def __init__(self ,name ,calories):
        self.name=name
        self.calories=calories
    def info(self):
        print(f"Food:{self.name}")
        print(f"calories:{self.calories}")

class Fruit(Food):
    def __init__(self,name,calories,is_sweet):
        super().__init__(name,calories)
        self.is_sweet=is_sweet
    def info(self):
        super().info()
        print(f"Sweet:{"Yes" if self.is_sweet else "no"}")

class Vegetable(Food):
    def __init__(self,name ,calories,is_leafy):
        super().__init__(name,calories)
        self.is_leafy=is_leafy

    def info(self):
        super().info()
        print(f"Leafy:{"Yes" if self.is_leafy else "no"}")

b= Fruit("banana",90,True)
b.info()
c =Vegetable("carrot",70, True)
c.info()



class Store:
    def __init__(self):
        self.inventory={}

    def add_product(self ,food_obj):
        self.inventory[food_obj.name.lower()]=food_obj

    def show_inventory(self):
        print("Available products: ")
        for item in self.inventory.values():
            item.info()
    def buy(self,product_name):
        name=product_name.lower()
        if name in self.inventory:
            return self.inventory[name]
        else:
            return None

class Smoothie:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

        total= 0
        for item in ingredients:
            total += item.calories
        self.total_calories=total

    def smoothie_info(self):
        print(f"Smoothie name: {self.name}")
        print("Ingredients: ")
        for item in self.ingredients:
            print("-",item.name)
        print("Total calories;",self.total_calories)



smarket = Store()
smarket.add_product(b)
smarket.add_product(c)
smarket.show_inventory()

smarket.add_product(Fruit("Apple",60,True))
smarket.add_product(Fruit("Tomato",40,False))
smarket.add_product(Vegetable("Kale",50,True))
smarket.add_product(Vegetable("Cucumber",10,True))

ingredients=[]
print("Welcome to the S-Market")
smarket.show_inventory()

while True:
    i =input("Add and ingredient to your smoothie(empty to finish): ")
    if i =="":
        break
    product=smarket.buy(i)
    if product:
        ingredients.append(product)
        print(f"Added {product.name}.")
    else:
        print("We don't have that here.")

if len(ingredients)== 0:
    print("No ingredients were found")

smoothie=Smoothie("best Smoothie",)






