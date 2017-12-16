import random

class Creature(object):
    creature_name = "Creature"
    base_health = 100
    base_speed = 100
    base_strength = 100
    base_intelligence = 100
    base_creativity = 100
    base_charisma = 100
    base_wickedness = 100

    def __init__(self):
        pass

class Human(Creature):
    creature = Creature()
    creature_type_base_health_modifier = 1.0
    creature_type_base_speed_modifier = 1.0
    creature_type_base_strength_modifier = 1.0
    creature_type_base_intelligence_modifier = 1.0
    creature_type_base_creativity_modifier = 1.0
    creature_type_base_charisma_modifier = 1.0
    creature_type_base_wickedness_modifier = 1.0
    creature_type_base_health = creature.base_health * creature_type_base_health_modifier
    creature_type_base_speed = creature.base_speed * creature_type_base_speed_modifier
    creature_type_base_strength = creature.base_strength * creature_type_base_strength_modifier
    creature_type_base_intelligence = creature.base_intelligence * creature_type_base_intelligence_modifier
    creature_type_base_creativity = creature.base_creativity * creature_type_base_creativity_modifier
    creature_type_base_charisma = creature.base_charisma * creature_type_base_charisma_modifier
    creature_type_base_wickedness = creature.base_wickedness * creature_type_base_wickedness_modifier

    creature_type = "Human"
    def __init__(self, name):
        self.name = name
        self.health = round(random.gauss(self.creature_type_base_health, self.creature_type_base_health*0.15), 3)
        self.speed = round(random.gauss(self.creature_type_base_speed, self.creature_type_base_speed*0.15), 3)
        self.strength = round(random.gauss(self.creature_type_base_strength, self.creature_type_base_strength*0.15), 3)
        self.intelligence = round(random.gauss(self.creature_type_base_intelligence, self.creature_type_base_intelligence*0.15), 3)
        self.creativity = round(random.gauss(self.creature_type_base_creativity, self.creature_type_base_creativity*0.15), 3)
        self.charisma = round(random.gauss(self.creature_type_base_charisma, self.creature_type_base_charisma*0.15), 3)
        self.wickendness = round(random.gauss(self.creature_type_base_wickedness, self.creature_type_base_wickedness*0.15), 3)
    
    def __repr__(self):
        attributes = "; ".join(["health: {}".format(self.health), "speed: {}".format(self.speed), "strength: {}".format(self.strength), "intelligence: {}".format(self.intelligence), "creativity: {}".format(self.creativity), "charisma: {}".format(self.charisma),"wickedness: {}".format(self.wickendness)])
        return "{} ({}) :: {}".format(self.name, self.creature_type, attributes)


class Elf(Creature):
    creature = Creature()
    creature_type_base_health_modifier = 1.9
    creature_type_base_speed_modifier = 1.3
    creature_type_base_strength_modifier = 0.7
    creature_type_base_intelligence_modifier = 2.0
    creature_type_base_creativity_modifier = 1.5
    creature_type_base_charisma_modifier = 1.3
    creature_type_base_wickedness_modifier = 0.3
    creature_type_base_health = creature.base_health * creature_type_base_health_modifier
    creature_type_base_speed = creature.base_speed * creature_type_base_speed_modifier
    creature_type_base_strength = creature.base_strength * creature_type_base_strength_modifier
    creature_type_base_intelligence = creature.base_intelligence * creature_type_base_intelligence_modifier
    creature_type_base_creativity = creature.base_creativity * creature_type_base_creativity_modifier
    creature_type_base_charisma = creature.base_charisma * creature_type_base_charisma_modifier
    creature_type_base_wickedness = creature.base_wickedness * creature_type_base_wickedness_modifier

    creature_type = "Elf"
    def __init__(self, name):
        self.name = name
        self.health = round(random.gauss(self.creature_type_base_health, self.creature_type_base_health*0.15), 3)
        self.speed = round(random.gauss(self.creature_type_base_speed, self.creature_type_base_speed*0.15), 3)
        self.strength = round(random.gauss(self.creature_type_base_strength, self.creature_type_base_strength*0.15), 3)
        self.intelligence = round(random.gauss(self.creature_type_base_intelligence, self.creature_type_base_intelligence*0.15), 3)
        self.creativity = round(random.gauss(self.creature_type_base_creativity, self.creature_type_base_creativity*0.15), 3)
        self.charisma = round(random.gauss(self.creature_type_base_charisma, self.creature_type_base_charisma*0.15), 3)
        self.wickendness = round(random.gauss(self.creature_type_base_wickedness, self.creature_type_base_wickedness*0.15), 3)

    def __repr__(self):
        attributes = "; ".join(["health: {}".format(self.health), "speed: {}".format(self.speed), "strength: {}".format(self.strength), "intelligence: {}".format(self.intelligence), "creativity: {}".format(self.creativity), "charisma: {}".format(self.charisma),"wickedness: {}".format(self.wickendness)])
        return "{} ({}) :: {}".format(self.name, self.creature_type, attributes)

class Orc(Creature):
    creature = Creature()
    creature_type_base_health_modifier = 0.7
    creature_type_base_speed_modifier = 0.6
    creature_type_base_strength_modifier = 2.0
    creature_type_base_intelligence_modifier = 0.5
    creature_type_base_creativity_modifier = 0.3
    creature_type_base_charisma_modifier = 0.3
    creature_type_base_wickedness_modifier = 0.4
    creature_type_base_health = creature.base_health * creature_type_base_health_modifier
    creature_type_base_speed = creature.base_speed * creature_type_base_speed_modifier
    creature_type_base_strength = creature.base_strength * creature_type_base_strength_modifier
    creature_type_base_intelligence = creature.base_intelligence * creature_type_base_intelligence_modifier
    creature_type_base_creativity = creature.base_creativity * creature_type_base_creativity_modifier
    creature_type_base_charisma = creature.base_charisma * creature_type_base_charisma_modifier
    creature_type_base_wickedness = creature.base_wickedness * creature_type_base_wickedness_modifier

    creature_type = "Orc"
    def __init__(self, name):
        self.name = name
        self.health = round(random.gauss(self.creature_type_base_health, self.creature_type_base_health*0.15), 3)
        self.speed = round(random.gauss(self.creature_type_base_speed, self.creature_type_base_speed*0.15), 3)
        self.strength = round(random.gauss(self.creature_type_base_strength, self.creature_type_base_strength*0.15), 3)
        self.intelligence = round(random.gauss(self.creature_type_base_intelligence, self.creature_type_base_intelligence*0.15), 3)
        self.creativity = round(random.gauss(self.creature_type_base_creativity, self.creature_type_base_creativity*0.15), 3)
        self.charisma = round(random.gauss(self.creature_type_base_charisma, self.creature_type_base_charisma*0.15), 3)
        self.wickendness = round(random.gauss(self.creature_type_base_wickedness, self.creature_type_base_wickedness*0.15), 3)

    def __repr__(self):
        attributes = "; ".join(["health: {}".format(self.health), "speed: {}".format(self.speed), "strength: {}".format(self.strength), "intelligence: {}".format(self.intelligence), "creativity: {}".format(self.creativity), "charisma: {}".format(self.charisma),"wickedness: {}".format(self.wickendness)])
        return "{} ({}) :: {}".format(self.name, self.creature_type, attributes)

def main():
    for i in range(50):
        marko = Human("Marko_{}".format(str(i).rjust(2, "0")))
        print(marko)
        glaenir = Elf("Glaenir_{}".format(str(i).rjust(2, "0")))
        print(glaenir)
        vidarok = Orc("Vidarok_{}".format(str(i).rjust(2, "0")))
        print(vidarok)

if __name__ == '__main__':
    main()