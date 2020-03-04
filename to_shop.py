from gets_and_posts import sell_treasure, move

from c_map import c_map

from to_room import to_room

from player import Player

from operations import Operations

# for api-key
from decouple import config


api_key = config('ADAM_KEY')

player = Player()
op = Operations()

def to_shop():
    current_room = op.init_player()
    path = to_room(current_room, 1, c_map=c_map)
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
        sell_treasure(item, api_key)
        #sell_treasure(item, API_KEY)
        print(f"You have {player.gold} now!")

to_shop()