import requests
from time import sleep
import json
from util import Queue, Move
from decouple import config

api_key = config('ADAM_KEY')

def starting_room():
    # grab the staring room data and store it in a list
    room_data = []
    start_room = {
        "room_id": 0,
        "title": "A brightly lit room",
        "description": "You are standing in the center of a brightly lit room. You notice a shop to the west and exits to the north, south and east.",
        "coordinates": "(60,60)",
        "players": [],
        "elevation": 0,
        "terrain": "NORMAL",
        "items": [],
        "exits": ["n", "s", "e", "w"],
        "cooldown": 1.0,
        "errors": [],
        "messages": []
    }    
    #res = requests.get("https://lambda-treasure-hunt.herokuapp.com/api/adv/init", headers={"Authorization": api_key})
    #data = res.json()    
    room_data.append(start_room)
    # put that data in a text file
    with open('room_data.txt', "w") as rd:
        rd.write(json.dumps(room_data))
    # create a file for room connections
    connecting_rooms = {}
    starting_room_connections = {"0": {'n': '?', 's': '?', 'e': '?', 'w': '?'}}
    connecting_rooms.update(starting_room_connections)
    # write to text file
    with open('connecting_rooms.txt', 'w') as conn:
        conn.write(json.dumps(connecting_rooms))

def explore(queue):
    room_id = str(room_data[-1]["room_id"])
    current_connections = connecting_rooms[room_id]
    unchecked_conns = []
    for direction in current_connections:
        if current_connections[direction] == "?":
            unchecked_conns.append(direction)

    if unchecked_conns:
        queue.enqueue(unchecked_conns[0])
    else:
        unchecked_paths = bft(room_data, connecting_rooms)
        if unchecked_paths is not None:
            for path in unchecked_paths:
                for direction in current_connections:
                    if current_connections[direction] == path:
                        queue.enqueue(direction)

def bft(room_data, connecting_rooms):
    cue = Queue()
    cue.enqueue([str(room_data[-1]["room_id"])])
    visited = set()

    while cue.size() > 0:
        room_list = cue.dequeue()
        room = room_list[-1]
        if room not in visited:
            visited.add(room)
            for direction in connecting_rooms[room]:
                if connecting_rooms[room][direction] == "?":
                    return room_list
                else:
                    path = list(room_list)
                    path.append(connecting_rooms[room][direction])
                    cue.enqueue(path)

starting_room()

with open("room_data.txt", "r") as rdata:
    room_data = json.loads(rdata.read())

with open("connecting_rooms.txt", "r") as rconn:
    connecting_rooms = json.loads(rconn.read())

cue2 = Queue()

explore(cue2)

while cue2.size() > 0:
    # Room info
    with open("room_data.txt", "r") as rdata:
        room_data = json.loads(rdata.read())
    # Room connections
    with open('connecting_rooms.txt', 'r') as rconn:
        connecting_rooms = json.loads(rconn.read())

    # Room player is in
    player_room = str(room_data[-1]["room_id"])
    direction = cue2.dequeue()
    # Move
    res = requests.post(Move, json={"direction": direction}, headers={'Authorization': api_key})
    data = res.json()
    room_data.append(data)
    # Redefine room player is in as they move
    new_room = str(room_data[-1]["room_id"])
    print(new_room)
    # Track that room in console
    print("now in room:" + str(new_room))
    connecting_rooms[player_room][direction] = new_room
    if new_room not in connecting_rooms:
        exits = data["exits"]
        directions = {}
        for xit in exits:
            directions[xit] = "?"
        connecting_rooms[new_room] = directions

    hol_up = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
    and_go_back = hol_up[direction]
    connecting_rooms[new_room][and_go_back] = player_room

    # Capture all that beautiful work
    with open('room_data.txt', 'w') as rdata:
        rdata.write(json.dumps(room_data))
    with open("connecting_rooms.txt", 'w') as rconn:
        rconn.write(json.dumps(connecting_rooms))
    sleep(data["cooldown"])
    explore(cue2)

    


