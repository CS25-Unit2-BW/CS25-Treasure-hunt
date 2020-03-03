from gets_and_posts import sell_treasure, move

from c_map import c_map

from to_room import to_room

from player import Player

# for api-key
from decouple import config


NISA_KEY = config('NISA_KEY')

player = Player()

def to_shop():
    path = to_room(player.current_room, 1, c_map=c_map)
    # path = bfs(current room, 1(shop room))
    length_of_path = len(path)
    # length of path in variable (easier to utilize)
    for m in path:
    # for loop of move in path:
        player.wise_explorer(m[0], m[1])
        #move player from move[0] to move[1] -- can use move or wise_explorer maybe?
        length_of_path -= 1
        #decrement length of path -1
    for item in player.inventory:
    # for item in player.inventory
        sell_treasure(item, NISA_KEY)
        #sell_treasure(item, API_KEY)
        print(f"You have {player.gold} now!")