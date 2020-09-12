class Critter:
    total = 0 

    @staticmethod
    def status():
        print("Общее число зверюшек", Critter.total)

    """Виртуальный питомец """
    def __init__(self, name, hunger = 0 , boredom = 0):
        self.name = name
        self.hunger = hunger 
        self.boredom = boredom 
        Critter.total += 1
    
    def talk(self):
        print("My name is ", self.name)

    def __str__(self):
        ans = "Объект класса Critter\n"
        ans += "имя: " + self.name + "\n"
        return ans    

def main():
    print("Доступ к атрибуту класса Critter.total: ",end = " " )
    print(Critter.total)

    print("Создание зверюшек. ")
    crit1 = Critter("Зверушка 1 ")
    crit2 = Critter("Зверушка 2 ")
    crit3 = Critter("Зверушка 3 ")
    
    Critter.status()

    print("Доступ к атрибуту класса через объект: ", end=" ")
    print(crit1.total)
main()            