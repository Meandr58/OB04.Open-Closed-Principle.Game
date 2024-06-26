# Шаг 1: Создание абстрактного класса для оружия
from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализация конкретных типов оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."
# Шаг 3: Модификация класса Fighter
class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        return self.weapon.attack()

# Шаг 4: Реализация боя
class Monster:
    def __init__(self, health: int):
        self.health = health

    def take_damage(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            return "Монстр побежден!"

def main():
    # Создание оружия
    sword = Sword()
    bow = Bow()

    # Создание бойца и монстра
    fighter = Fighter(sword)
    monster = Monster(health=10)

    # Боец атакует монстра мечом
    print("Боец выбирает меч.")
    print(fighter.attack())
    print(monster.take_damage(10))

    # Боец меняет оружие на лук
    print("Боец выбирает лук.")
    fighter.changeWeapon(bow)
    print(fighter.attack())
    print(monster.take_damage(10))

if __name__ == "__main__":
    main()
