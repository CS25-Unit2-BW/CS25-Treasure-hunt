from util import Queue
from c_map import c_map

"""
prints both the room list and the directional path
returns the directional path
"""

# only requires the start_room, and destination, c_map is the default map
# destiniation is the room id of the destination room
def to_room(start_room, destination, c_map = c_map):
        # print(c_map.neighbors)
        queue = Queue()
        direct = Queue()
        visited = set()
        # add the path to the starting room (including entire room) to the queue
        queue.enqueue([start_room])
        direct.enqueue([])
        while queue.size() > 0:
        
            path = queue.dequeue()
            # removed the last (entire) room from the queue
            # should be a full room
            room = path[-1]
            # print(room)
            directions = direct.dequeue()

            if room["room_id"] == destination:
                print(f"path: {path}")
                print(f"directions: {directions}")
                return directions
            elif room["room_id"] in visited:
                continue
            else:
                visited.add(room["room_id"])
                # get adjacent edges and add to back of path by pulling neighbors from the room object
                neighbors = room["neighbors"]
                for direction in neighbors:
                    # make a copy of the path
                    new_path = path.copy()
                    new_direct = directions.copy()
                    # get the room associated with the direction
                    new_room = int(neighbors[direction])
                    neighbor = c_map[new_room]
                    # add neighbor to the back of that path
                    new_path.append(neighbor)
                    new_direct.append(direction)
                    # add the path to the queue
                    queue.enqueue(new_path)
                    direct.enqueue(new_direct)


# use to test
# to_room(c_map[467], 1)