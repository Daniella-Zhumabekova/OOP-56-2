
class Hero:
    #Конструктор класса
    def __init__(self, name, lvl, hp):
        #атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp
    #метод класса
    def introduce(self):
        return print(f"привет меня зовут {self.name}")

#объект класса
kirito = Hero("kirito", 100, "1000")
asuna = Hero("asuna", 200, "1250")

kirito.introduce()
asuna.introduce()
print(kirito.name, kirito.lvl)
print(asuna.name, asuna.lvl)



