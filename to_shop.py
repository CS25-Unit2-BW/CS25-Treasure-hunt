from gets_and_posts import sell_treasure, move

from c_map import c_map

from to_room import to_room

from player import Player

from operations import Operations

import sys

# for api-key
from decouple import config


api_key = config('API_KEY')

player = Player()

operations = Operations()

def to_shop(c_map=c_map):
    current_room = operations.init_player()

    check_inv = operations.check_status()


    cur_room_id = current_room['room_id']
    path = to_room(c_map[cur_room_id], 1)
    length_of_path = len(path)
    if current_room['title'] == 'Shop':
        for item in check_inv['inventory']:
            operations.sell(item)
            print(f"You have {check_inv['gold']} now!")
    else:
        for m in path:
            print(m, 'THIS ONE')
            print(current_room['room_id'],current_room['title'],'NOW LOOK')
            operations.move(m)
            length_of_path -= 1



print(to_shop())