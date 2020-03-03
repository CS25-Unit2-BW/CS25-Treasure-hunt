from c_map import c_map
from c_rooms import connect


# original purpose was to read the text files
# it was finally just used to create the full map
def map_reader():
    for fr in c_map:
        for cr in connect:
            if int(fr) == int(cr):
                c_map[fr]["neighbors"] = connect[cr]
    print(c_map)
    


    # with open('room_data.txt') as rd:
    #     for line in rd:
    #         map_d = line
    #         print(map_d)
    #         for room in map_d:
    #             print('new line')
    #             print(room)
    #         # room_one = line.split(":")[:14]
    #         # for r in room_one:
    #         #     foo = r.split(",")
    #         #     for s in foo:
    #         #         t=s.translate({ord('{'):None}).translate({ord('['):None}).translate({ord(']'):None}).translate({ord('}'):None}).strip()
    #         #         if t == "room_id":
    #         #             print(t)
map_reader()
