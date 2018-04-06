class Item(object):
    def __init__(self, name, description, room, picked):
        self.name = name
        self.desc = description
        self.room = room
        self.pick = picked

    def drop(self):
        self.pick = True


class Consumable(Item):
    def __init__(self, name, description, room, picked):
        self.used = False
        super(Consumable, self).__init__(name, description, room, picked)

    def use(self):
        self.used = True
        print("You used %s" % self.name)


class Weapon(Item):
    def __init__(self, name, description, room, picked, health_taken):
        self.health = health_taken
        super(Weapon, self).__init__(name, description, room, picked)

    def attack(self, target):
        print("You attacked %s with %s" % (target, self.name))


class Container(Item):
    def __init__(self, name, description, room, picked, space):
        self.space = space
        self.open = False
        super(Container, self).__init__(name, description, room, picked)

    def open(self):
        self.open = True
        print("You opened your backpack.")

    def close(self):
        self.open = False
        print("You closed your backpack.")


class Defense(Item):
    def __init__(self, name, description, room, picked, damage_reduced):
        self.worn = False
        self.damage = damage_reduced
        super(Defense, self).__init__(name, description, room, picked)

    def wear(self):
        self.worn = True
        print("You put on the %s" % self.name)

    def take_off(self):
        self.worn = False
        print("You took off the %s" % self.name)


class Melee(Weapon):
    def __init__(self, name, description, room, picked, health_taken):
        super(Melee, self).__init__(name, description, room, picked, health_taken)

    def slash(self, target):
        self.attack(target)


class BadMelee(Melee):
    def __init__(self, name, description, room, picked, health_taken, durability):
        self.durability = durability
        super(BadMelee, self).__init__(name, description, room, picked, health_taken)

    def destruct(self):
        print("%s has been broken!" % self.name)


class Food(Consumable):
    def __init__(self, name, description, room, picked, hunger_restored):
        self.hunger = hunger_restored
        super(Food, self).__init__(name, description, room, picked)

    def eat(self):
        self.used = True
        print("You ate %s" % self.name)


class Beverage(Consumable):
    def __init__(self, name, description, room, picked, thirst_restored):
        self.thirst = thirst_restored
        super(Beverage, self).__init__(name, description, room, picked)

    def drink(self):
        self.used = True
        print("You drank %s" % self.name)


class BadFood(Food):
    def __init__(self, name, description, room, picked, hunger_restored, health_taken):
        self.health = health_taken
        super(BadFood, self).__init__(name, description, room, picked, hunger_restored)

    def eat(self):
        self.used = True
        self.health -= 10
        print("You ate %s but it made you feel sick." % self.name)


class BadBeverage(Beverage):
    def __init__(self, name, description, room, picked, thirst_restored, health_taken):
        self.health = health_taken
        super(BadBeverage, self).__init__(name, description, room, picked, thirst_restored)

    def drink(self):
        self.used = True
        self.health -= 10
        print("You drank %s, but it made you feel sick." % self.name)


class Healing(Consumable):
    def __init__(self, name, description, room, picked, health_restored):
        self.health = health_restored
        super(Healing, self).__init__(name, description, room, picked)

    def heal(self, heal_amount):
        self.health -= heal_amount


class Bag(Container):
    def __init__(self, name, description, room, picked, space):
        super(Bag, self).__init__(name, description, room, picked, space)

    def crumple(self):
        self.pick = False
        print("You crumpled up your bag.")


class Backpack(Container):
    def __init__(self, name, description, room, picked, space):
        super(Backpack, self).__init__(name, description, room, picked, space)

    def throw(self, health_taken, target):
        self.pick = False
        print("You threw your backpack at %s." % target)


class HeavyBackpack(Container):
    def __init__(self, name, description, room, picked, space):
        super(HeavyBackpack, self).__init__(name, description, room, picked, space)

    def slam(self, health_taken, target):
        print("You slammed your backpack into %s!" % target)


lantern = Item("Lantern", "yuh", "light", False)
