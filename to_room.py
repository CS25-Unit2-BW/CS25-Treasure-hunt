from util import Queue
from c_map import c_map

"""
i want this to return a list of rooms
then convert the list of room into directions for "move"
"""
def get_room(room_id, c_map=c_map):
    return c_map[room_id]
# only requires the start_room, and destination, c_map is the default map
# destiniation is the room id of the destination room
def to_room(start_room, destination, c_map = c_map):
        queue = Queue()
        
        visited = set()
        # add the path to the starting room (including entire room) to the queue
        queue.enqueue([start_room])
        
        while queue.size() > 0:
        
            path = queue.dequeue()
            # removed the last (entire) room from the queue
            # should be a full room
            room = path[-1]
            # print(room)

            if room["room_id"] == destination:
                print(f"path: {path}")
                return path
            elif room["room_id"] in visited:
                continue
            else:
                visited.add(room["room_id"])
                # get adjacent edges and add to back of path by pulling neighbors from the room object
                neighbors = room["neighbors"]
                for direction in neighbors:
                    # make a copy of the path
                    new_path = path.copy()
                    # get the room associated with the direction
                    new_room = int(neighbors[direction])
                    neighbor = c_map[new_room]
                    # add neighbor to the back of that path
                    new_path.append(neighbor)
                    # add the path to the queue
                    queue.enqueue(new_path)

# use to test
# to_room(c_map[467], 1)