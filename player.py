# for api-key
from decouple import config

import requests
import json
from util import Wise_Explorer,Init,Inventory

NISA_KEY = config('NISA_KEY')

class Player:
    def __init__(self):
        self.init()
        self.status()

    def init(self):
        header = {
                "Authorization": f"Token {NISA_KEY}",
                "Content-Type": "application/json",
        }

        response = requests.get(
            Init,
            headers = header,
        )
        self.current_room = response["room_id"]
        self.room_items = response["items"]
        self.room_exits = response["exits"]
        self.errors = response["errors"]
        self.messages = response["messages"]
        self.cooldown = response["cooldown"]
        return response

    def status(self):
        header = {
                "Authorization": f"Token {NISA_KEY}",
                "Content-Type": "application/json",
        }

        response = requests.get(
            Inventory,
            headers = header,
        )
        self.name = response["name"]
        self.encumbrance = response["encumbrance"]
        self.strength = response["strength"]
        self.speed = response["speed"]
        self.gold = response["gold"]
        self.inventory = response["inventory"]
        self.errors = response["errors"]
        self.messages = response["messages"]
        self.bodywear = None
        self.footwear = None
        self.abilities = []
        return response
    


    def wise_explorer(self, direction, room_id):
        header = {
            "Authorization": f"Token {NISA_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post(
            Wise_Explorer,
            headers=header,
            data=json.dumps({"direction": direction, "next_room_id": str(room_id)}),
            cooldown=self.cooldown
        )

        self.current_room = response["room_id"]
        self.room_items = response["items"]
        self.room_exits = response["exits"]
        self.errors = response["errors"]
        self.messages = response["messages"]
        self.cooldown = response["cooldown"]
        return response