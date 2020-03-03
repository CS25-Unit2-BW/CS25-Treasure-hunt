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

api_key = config('ADAM_KEY')


class Operations:
    def __init__(self):
        self.current_room = {}
    
    def init_player(self):
        res = requests.get(Init, headers={"Authorization": api_key}).json()
        self.wait = float(res.get('cooldown'))
        self.current_room = res
        sleep(res['cooldown'])
        print(self.current_room)
        return self.current_room
        
Operations().init_player()