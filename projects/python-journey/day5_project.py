from abc import ABC, abstractmethod
class Character(ABC):
    total_characters = 0
    def __init__(self,name,health,attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        Character.total_characters +=1
    @abstractmethod
    def special_attack(self):
        pass

    def take_damage(self,amount):
        self.health = self.health - amount
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def __str__(self):
        return (f"Character: [self.name] | HP: [self.health]")
class Warrior(Character):
    def __init__(self,name,health,attack_power):

        super().__init__(name,health,attack_power)
        self.shield = 100
    def special_attack(self):
        print(f"{self.name} slashes with sword! deals 50 damage")
    def block(self):
        print(f"{self.name} blocks with shield! shield: {self.shield}")
    def __str__(self):
        return(f"Warrior: {self.name} | HP: {self.health} | Shield: {self.shield}")
    
class Mage(Character):
    def __init__(self,name, health, attack_power):
        super().__init__(name, health, attack_power)
        self.mana = 100
    def special_attack(self):
        print(f"{self.name} casts Fireball! deals 80 damage")
    def cast_spell(self):
        self.mana -= 10 
        print(f"{self.name} casts a spell! Mana left: {self.mana}")
    def __str__(self):
        return(f"Mage: {self.name} | HP: {self.health} | Mana: {self.mana}")
    

if __name__ == "__main__":
    w = Warrior("Alvar", 100, 30)
    m = Mage("Gandalf", 80, 20)
    
    print(w)
    print(m)
    
    w.special_attack()
    m.special_attack()
    
    w.take_damage(30)
    print(w.is_alive())
    print(w)
    
    w.block()
    m.cast_spell()
    
    print(Character.total_characters)

    


