from gets_and_posts import sell_treasure, move

from c_map import c_map

from to_room import to_room

from player import Player

from operations import Operations

# for api-key
from decouple import config


api_key = config('API_KEY')

player = Player()

operations = Operations()

def to_change_name(c_map=c_map):
    current_room = operations.init_player()

    check_inv = operations.check_status()
    print('CHECK INVENTORY', check_inv['inventory'])

    print(current_room, 'LOOKIE')
    print(current_room['room_id'],current_room['title'],'NOW LOOK')
    print(current_room['title'], 'NOW LOOK')
    cur_room_id = current_room['room_id']
    path = to_room(c_map[cur_room_id], 467)
    # path = bfs(current room, 1(shop room))
    length_of_path = len(path)
    print(length_of_path)
    if current_room['title'] == "Pirates Ry's":
        operations.change_name('BUM')
    else:
        for m in path:
            # for loop of move in path:
            print(current_room['room_id'],current_room['title'],'NOW LOOK')
            player.move(m)
            length_of_path -= 1


print(to_change_name())