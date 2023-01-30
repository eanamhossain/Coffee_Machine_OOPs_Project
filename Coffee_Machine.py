class CoffeeMachine:
    def __init__(self, water, milk, coffeeBeans, disposableCups, money):
        self.water = water
        self.milk = milk
        self.coffeeBeans = coffeeBeans
        self.disposableCups = disposableCups
        self.money = money

        self.showSupply()
        self.Buy()


    def showSupply(self):
        print("The coffee machie has:")
        print(self.water, "Of water")
        print(self.milk , "Of milk")
        print(self.coffeeBeans, "Of coffeeBeans")
        print(self.disposableCups   , "Of disposableCups")
        print(self.money   , "Of money")

    
    def Buy(self):
        buy = input("""
        
        "What do you want to buy? 
        1 - espresso, 
        2 - latte, 
        3 - cappuccino, 
        back - to main menu"
        
        """)

        if buy == '1' :
            self.Espresso()
        elif buy == '2' :
            self.Latte()
        elif buy == '3' :
            self.Cappuccino()
        else:
            print("Please ,Choose Your coffee")

    
    def Espresso(self):
        self.w = 250
        self.m = 0
        self.c = 16
        self.d = 1
        self.my = 4

        if self.water > self.w and self.milk > self.m and self.coffeeBeans > self.c and self.disposableCups > self.d and self.money > self.my :
            self.water = self.water - self.w 
            self.milk = self.milk  - self.m
            self.coffeeBeans = self.coffeeBeans - self.c
            self.disposableCups = self.disposableCups - self.d
            self.money = self.money - self.my
            print("Your coffee Espresso is ready!")

        else:
            print(" Sorry ")


    def Latte(self):
        self.w = 350
        self.m = 75
        self.c = 20
        self.d = 1
        self.my = 7

        if self.water > self.w and self.milk > self.m and self.coffeeBeans > self.c and self.disposableCups > self.d and self.money > self.my :
            self.water = self.water - self.w 
            self.milk = self.milk  - self.m
            self.coffeeBeans = self.coffeeBeans - self.c
            self.disposableCups = self.disposableCups - self.d
            self.money = self.money - self.my
            print("Your coffee Latte is ready!")

        else:
            print(" Sorry ")


    def Cappuccino(self):
        self.w = 200
        self.m = 100
        self.c = 12
        self.d = 1
        self.my = 6

        if self.water > self.w and self.milk > self.m and self.coffeeBeans > self.c and self.disposableCups > self.d and self.money > self.my :
            self.water = self.water - self.w 
            self.milk = self.milk  - self.m
            self.coffeeBeans = self.coffeeBeans - self.c
            self.disposableCups = self.disposableCups - self.d
            self.money = self.money - self.my
            print("Your coffee Cappuccino is ready!")

        else:
            print(" Sorry ")            

my_coffee = CoffeeMachine(2000,200,100,20,100)

# my_coffee.Espresso()
# my_coffee.Latte()
# my_coffee.Cappuccino()

print("Machine water now: ",my_coffee.water)
print("Machine milk now: ",my_coffee.milk)
print("Machine coffeeBeans now: ",my_coffee.coffeeBeans)
print("Machine money now: ",my_coffee.money)
print("Machine disposableCups now: ",my_coffee.disposableCups)
