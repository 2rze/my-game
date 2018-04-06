class Character(object):
    def __init__(self, name, description, current_hp):
        self.name = name
        self.desc = description
        self.c_hp = current_hp


class Player(Character):
    def __init__(self, name, description, current_hp, inventory_space, current_position):
        self.space = inventory_space
        self.c_pos = current_position
        super(Player, self).__init__(name, description, current_hp)

    def damage(self, amount):
        self.c_hp -= amount
        print("You've lost %d health!")

    def take(self, item):
        print("You have taken %s", item)
        self.space -= item.weight


class Enemy(Character):
    def __init__(self, name, description, current_hp, current_room, weapon_drop):
        self.room = current_room
        self.weap = weapon_drop
        super(Enemy, self).__init__(name, description, current_hp)

    def attack(self, amount):
        print("%s attacked you!" % self.name)
        player.damage(amount)

    def death(self):
        print("%s has died." % self.name)


name = input("What's your name?\n")
desc = input("Give yourself a description.\n")
player = Player(name, desc, 100, 100, "lightroom")

""" 
    # I'm probably going to include more characters later, which means I'm probably going to remove some of these later
    # Just a heads up ¯\_(ツ)_/¯
"""

shriek = Enemy("Shriek", "You've encountered a Shriek, kill it before it attracts more!", 75, "hallway", None)
overseer = Enemy("Overseer", "You've encountered an Overseer, be prepared to take hits!", 400, "hole", "Energy Blade")
