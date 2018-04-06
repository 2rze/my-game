class Room(object):
    def __init__(self, name, description, north, south, east, west):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def move(self, direction):
        global cur
        cur = globals()[getattr(self, direction)]


"""class Character(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def killed(self):
        exit("he are die :(")


bob = Character("jeff", "his name jeff")"""

light = Room("Light Room", "You are in a room with a dimly lit light.", None, None, None, "hallw")
hallw = Room("Hallway", "You are in a dark hallway.", None, "inter", "light", None)
dark1 = Room("Dark Room", "You are in a dark room, and you hear crunching noises.", None, None, "hallw", None)
dark2 = Room("Dark Room", "You are in a dark room, and you hear crunching noises.", None, None, "hallw", None)
eleva = Room("Elevator", "You enter an elevator, but immediately realize it's unstable.", None, None, None, "hallw")
restr = Room("Restroom", "You enter a restroom, and get hit with a strong odor.", None, None, None, "hallw")
close = Room("Closet", "You enter a small closet.", None, None, None, "hallw")

inter = Room("Intersection", "You are at an intersection. West is a bridge, and South are a set of stairs.", None,
             "stair", "bridg", None)
stair = Room("Stairs", "You step onto the set of stairs. You see a room that is lit up below.", "inter",
             "loung", None, None)
bridg = Room("Bridge", "You are on a bridge, with paths every direction, except North.", None, "piitt",
             "autho", "inter")
space = Room("Space", "You immediately feel the oxygen leave your lungs.", None, None, None, None)

loung = Room("Lounge", "You are in a room that seems to have been trashed.", "stair", None, "piitt", None)

piitt = Room("Pit", "You are in front of a large pit.", "bridg", "holee", None, "loung")
holee = Room("Hole", "You are in front of a large hole.", "piitt", None, None, None)

autho = Room("Security Building", "You are in front of a building wth a large sign that says 'SECURITY BUILDING'",
             None, None, "maint", None)
maint = Room("Maintenance", "You are in a room with pathways in every direction.",
             "camer", "locke", "chute", "autho")
camer = Room("Camera Room", "You are in a room with screens viewing every location that you've been in.",
             None, "maint", None, None)
chute = Room("Chute", "You are in a room with what looks like a door with a window.", None, None, "space",
             "maint")
locke = Room("Locker Room", "You are in a locker room.", "maint", None, None, None)

Dir = ['north', 'south', 'east', 'west']
s_Dir = ['n', 's', 'e', 'w']
cur = light

while True:
    cmd = input("> ").lower().strip()
    if cmd == "quit" or cmd == "die" or cmd == "suicide" or cmd == "kill self":
        print("You were killed.")
        quit(0)
    elif cmd in s_Dir:
        pos = s_Dir.index(cmd)
        cmd = Dir[pos]
    if cmd in Dir:
        if cur == space:
            print("You are dead.")
            quit(0)
        elif cmd == "north" and cur == bridg:
            print("I just told you that you can't go North.")
        else:
            try:
                cur.move(cmd)
                print(cur.name + '\n' + cur.description)
            except KeyError:
                print("You can't go that way.")
    elif cmd == "look":
        print(cur.name, '\n', cur.description)
    elif cmd == "hi":
        print("hi lol")
    else:
        print("Command doesn't exist.")
