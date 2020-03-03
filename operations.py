import requests
from time import sleep
import json 
import hashlib
import random
from decouple import config
from util import (Init, Coin_Balance, Last_Proof, 
Move, 
Wise_Explorer,
Take, 
Drop, 
Sell, 
Examine, 
Inventory,  
Wear,  
Undress,  
Change_your_name,  
Pray,  
Fly,  
Dash, 
Carry, 
Receive,
Warp, 
Mine)
#from map_reader import map_reader


api_key = config('ADAM_KEY')


class Operations:
    def __init__(self):
        self.current_room = {}
    
    def init_player(self):
        res = requests.get(Init, headers={"Authorization": api_key}).json()       
        self.wait = float(res.get('cooldown'))
        self.current_room = res
        sleep(res['cooldown'])        
        return self.current_room

    def room_id(self):
        return self.current_room['room_id']

    def move(self, direction):
        if direction not in self.current_room['exits']:
            print("You can't go that way")
            return
        else:
            res = requests.post(Move, json={'direction': direction}, headers={'Authorization': api_key}).json()
            self.current_room = res
            sleep(res['cooldown'])
            return self.current_room

    def take(self):
        if len(self.current_room['items']) == 0:
            print("Nothing here to take")
            return None
        else:
            item = self.current_room["items"]
            print(f"taking {item}")
            res = requests.post(Take, json={"name": item[0]}, headers={"Authorization": api_key}).json()
            sleep(res["cooldown"])

    def sell(self, item="tiny treasure"):
        if self.current_room["title"] != 'Shop':
            print("This isn't a shop buddy!")
        else:
            res1 = requests.post(Sell, json={"name": item}, headers={'Authorization': api_key}).json()
            print(res1)
            sleep(res1['cooldown'])
            res = requests.post(Sell, json={"name": item, "confirm": "yes"}, headers={'Authorization': api_key}).json()
            print(res)
            sleep(res['cooldown'])

    def change_name(self, name):
        if self.current_room['title'] != "Pirate Ry's":
            print("Only a pirate can you give a name don't ya know!")
        else:
            res = requests.post(Change_your_name, json={"name": [name], "confirm": 'aye'}, headers={'authorization': api_key}).json()
            print("You shall be known as", str(name))
            print(res)
            return res

    def check_status(self):
        res = requests.post(Inventory, headers={"Authorization": api_key}).json()
        print(res)
        sleep(res['cooldown'])



        
