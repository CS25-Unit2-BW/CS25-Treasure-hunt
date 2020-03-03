class Player:
    def __init__(self, starting_room, name="User"):
        self.name = name,
        self.cooldown = 1
        self.encumbrance = 0,
        self.strength = 10,
        self.speed = 10,
        self.gold = 0,
        self.bodywear = None,
        self.footwear = None,
        self.inventory = [],
        self.abilities = [],
        self.status = [],
        self.has_mined = False,
        self.errors = [],
        self.messages = []
        self.current_room = starting_room