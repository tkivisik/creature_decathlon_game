import random

class Creature(object):
    creature_name = "Creature"
    base_health = 100.0
    base_speed = 100.0
    base_strength = 100.0
    base_intelligence = 100.0
    base_creativity = 100.0
    base_charisma = 100.0
    base_wickedness = 100.0

    def __init__(self, name, creature_type, base_health, base_speed, base_strength, base_intelligence, base_creativity, base_charisma, base_wickedness):
        self.name = name
        self.creature_type = creature_type
        self.health = round(random.gauss(base_health, base_health*0.15), 3)
        self.speed = round(random.gauss(base_speed, base_speed*0.15), 3)
        self.strength = round(random.gauss(base_strength, base_strength*0.15), 3)
        self.intelligence = round(random.gauss(base_intelligence, base_intelligence*0.15), 3)
        self.creativity = round(random.gauss(base_creativity, base_creativity*0.15), 3)
        self.charisma = round(random.gauss(base_charisma, base_charisma*0.15), 3)
        self.wickendness = round(random.gauss(base_wickedness, base_wickedness*0.15), 3)

    def __repr__(self):
        attributes = "; ".join(["health: {}".format(self.health), "speed: {}".format(self.speed), "strength: {}".format(self.strength), "intelligence: {}".format(self.intelligence), "creativity: {}".format(self.creativity), "charisma: {}".format(self.charisma),"wickedness: {}".format(self.wickendness)])
        return "{} ({}) :: {}".format(self.name, self.creature_type, attributes)

class Human(Creature):
    base_health_modifier = 1.0
    base_speed_modifier = 1.0
    base_strength_modifier = 1.0
    base_intelligence_modifier = 1.0
    base_creativity_modifier = 1.0
    base_charisma_modifier = 1.0
    base_wickedness_modifier = 1.0
    base_health = Creature.base_health * base_health_modifier
    base_speed = Creature.base_speed * base_speed_modifier
    base_strength = Creature.base_strength * base_strength_modifier
    base_intelligence = Creature.base_intelligence * base_intelligence_modifier
    base_creativity = Creature.base_creativity * base_creativity_modifier
    base_charisma = Creature.base_charisma * base_charisma_modifier
    base_wickedness = Creature.base_wickedness * base_wickedness_modifier

    creature_type = "Human"
    def __init__(self, name):
        Creature.__init__(self, name, self.creature_type, self.base_health, self.base_speed, self.base_strength, self.base_intelligence, self.base_creativity, self.base_charisma, self.base_wickedness)

class Elf(Creature):
    base_health_modifier = 1.9
    base_speed_modifier = 1.3
    base_strength_modifier = 0.7
    base_intelligence_modifier = 2.0
    base_creativity_modifier = 1.5
    base_charisma_modifier = 1.3
    base_wickedness_modifier = 0.3
    base_health = Creature.base_health * base_health_modifier
    base_speed = Creature.base_speed * base_speed_modifier
    base_strength = Creature.base_strength * base_strength_modifier
    base_intelligence = Creature.base_intelligence * base_intelligence_modifier
    base_creativity = Creature.base_creativity * base_creativity_modifier
    base_charisma = Creature.base_charisma * base_charisma_modifier
    base_wickedness = Creature.base_wickedness * base_wickedness_modifier

    creature_type = "Elf"
    def __init__(self, name):
        Creature.__init__(self, name, self.creature_type, self.base_health, self.base_speed, self.base_strength, self.base_intelligence, self.base_creativity, self.base_charisma, self.base_wickedness)

class Orc(Creature):
    base_health_modifier = 0.7
    base_speed_modifier = 0.6
    base_strength_modifier = 2.0
    base_intelligence_modifier = 0.5
    base_creativity_modifier = 0.3
    base_charisma_modifier = 0.3
    base_wickedness_modifier = 0.4
    base_health = Creature.base_health * base_health_modifier
    base_speed = Creature.base_speed * base_speed_modifier
    base_strength = Creature.base_strength * base_strength_modifier
    base_intelligence = Creature.base_intelligence * base_intelligence_modifier
    base_creativity = Creature.base_creativity * base_creativity_modifier
    base_charisma = Creature.base_charisma * base_charisma_modifier
    base_wickedness = Creature.base_wickedness * base_wickedness_modifier

    creature_type = "Orc"
    def __init__(self, name):
        Creature.__init__(self, name, self.creature_type, self.base_health, self.base_speed, self.base_strength, self.base_intelligence, self.base_creativity, self.base_charisma, self.base_wickedness)

def create_creatures(creature_type, n):
    list_of_creatures = []
    for i in range(n):
        list_of_creatures.append()
    return list_of_creatures

def main():
    if True:
        for i in range(50):
            marko = Human("Marko_{}".format(str(i).rjust(2, "0")))
            print(marko)
            glaenir = Elf("Glaenir_{}".format(str(i).rjust(2, "0")))
            print(glaenir)
            vidarok = Orc("Vidarok_{}".format(str(i).rjust(2, "0")))
            print(vidarok)

if __name__ == '__main__':
    main()
