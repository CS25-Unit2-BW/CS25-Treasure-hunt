import json
import requests

from mine import proof_of_work, valid_proof
from util import Move,Mine,Init,Receive,Inventory,Dash,Carry, Wear,Warp,Wise_Explorer,Fly ,Pray,Drop, Last_Proof,Coin_Balance,Sell,Take,Examine,Change_your_name

# for api-key
from decouple import config

NISA_KEY = config('NISA_KEY')

header = {
    'Authorization': f"Token: {NISA_KEY}",
    'Content-Type': 'application/json',
}

def init(NISA_KEY):
    header
    response = requests.get(
        Init,
        headers = header,
        data = json.dumps({})
    )
    return response

# MOVEMENT ENDPOINTS
def move(direction, NISA_KEY):
    header
    response = requests.post(
        Move,
        headers = header,
        data = json.dumps({'direction': direction})
    )
    return response

def wise_explorer(direction, room_id, NISA_KEY):
    header
    response = requests.post(
        Wise_Explorer,
        headers = header,
        data = json.dumps({'directions': direction, 'Next Rooms Id': str(room_id)})
    )
    return response


# TREASURE ENDPOINTS
def pickup_treasure(treasure, NISA_KEY):
    header
    response = requests.post(
        Take,
        headers = header,
        data = json.dumps({'name': treasure})
    )
    return response

def examine(treasure_name, player_name, NISA_KEY):
    header
    response = requests.post(
        Examine,
        headers=header,
        data=json.dumps({"name":f"{treasure_name or player_name}"}),
    )
    return response

def drop_treasure(treasure, NISA_KEY):
    header
    response = requests.post(
        Drop,
        headers = header,
        data=json.dumps({'Name': f"{treasure}"})
    )
    return response

def sell_treasure(treasure, NISA_KEY):
    header
    response = requests.post(
        Sell,
        headers = header,
        data=json.dumps({"Name": f"{treasure}", "Confirm": "yes"})
    )
    return response

def status_inventory(NISA_KEY):
    header
    response = requests.post(
        Inventory,
        headers=header,
        data=json.dumps({}),
    )
    return response

def name_change(name, NISA_KEY):
    header
    response = requests.post(
        Change_your_name,
        headers=header,
        data=json.dumps({'Name': f"{name}"})
    )
    return response

def pray_at_shrine(NISA_KEY):
    header
    response=requests.post(
        Pray,
        headers=header,
        data = json.dumps({})
    )
    return response

def fly(direction, NISA_KEY):
    header
    response = requests.post(
        Fly,
        headers = header,
        data = json.dumps({'direction': f"{direction}"})
    )
    return response

def dash(direction, num_rooms, room_id, NISA_KEY):
    header
    response = requests.post(
        Dash,
        headers = header,
        data = json.dumps({'direction': f"{direction}", 'Number of rooms': f"{num_rooms}", 'Next Room Id': f"{room_id}"})
    )
    return response

def carry(item_name, NISA_KEY):
    header
    response = requests.post(
        Carry,
        headers = header,
        data = json.dumps({'Item Name': f"{item_name}"})
    )
    return response

def receive(NISA_KEY):
    header
    response = requests.post(
        Receive,
        headers = header,
        data = json.dumps({})
    )
    return response
    

def warp(NISA_KEY):
    header
    response = requests.post(
        Warp,
        headers = header,
        data = json.dumps({})
    )
    return response

def mine(proof, NISA_KEY):
    pass

def get_last_proof(NISA_KEY):
    pass

def get_balance(NISA_KEY):
    pass

def transmogrify(item_name, NISA_KEY):
    pass