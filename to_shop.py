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
<<<<<<< HEAD
    #print('CHECK INVENTORY', check_inv['inventory'])

    #print(current_room, 'LOOKIE')
    #print(current_room['room_id'],current_room['title'],'NOW LOOK')
    #print(current_room['exits'], 'NOW LOOK')
    cur_room_id = current_room['room_id']
    path = to_room(c_map[cur_room_id], 105)
    # path = bfs(current room, 1(shop room))
    print("path", path)
    length_of_path = len(path)
    # if current_room['title'] == 'Shop':
    #     for item in check_inv['inventory']:
    #         operations.sell(item)
    #         #print(f"You have {check_inv['gold']} now!")
    #else:
    for m in path:
            # for loop of move in path:
        print(m, 'THIS ONE')
            #print(current_room['room_id'],current_room['title'],'NOW LOOK')
        operations.move(m)
        length_of_path -= 1
=======

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
>>>>>>> dcbae83402d926f062a4a0db47151ef93677bf3b


print(to_shop())