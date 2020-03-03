class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)

    #GET

Init = "https://lambda-treasure-hunt.herokuapp.com/api/adv/init"
Coin_Balance = "https://lambda-treasure-hunt.herokuapp.com/api/adv/get_balance"
Last_Proof = "https://lambda-treasure-hunt.herokuapp.com/api/adv/last_proof"



    #POST 

Move = "https://lambda-treasure-hunt.herokuapp.com/api/adv/move"
Wise_Explorer =" https://lambda-treasure-hunt.herokuapp.com/api/adv/move"
Take = "https://lambda-treasure-hunt.herokuapp.com/api/adv/take"
Drop = "https://lambda-treasure-hunt.herokuapp.com/api/adv/drop"
Sell = "https://lambda-treasure-hunt.herokuapp.com/api/adv/sell"
Examine = "https://lambda-treasure-hunt.herokuapp.com/api/adv/examine"
Inventory = "https://lambda-treasure-hunt.herokuapp.com/api/adv/status"
Wear = "https://lambda-treasure-hunt.herokuapp.com/api/adv/wear"
Undress = "https://lambda-treasure-hunt.herokuapp.com/api/adv/undress"
Change_your_name = "https://lambda-treasure-hunt.herokuapp.com/api/adv/change_name"
Pray = "https://lambda-treasure-hunt.herokuapp.com/api/adv/pray"
Fly = "https://lambda-treasure-hunt.herokuapp.com/api/adv/fly"
Dash = "https://lambda-treasure-hunt.herokuapp.com/api/adv/dash"
Carry = "https://lambda-treasure-hunt.herokuapp.com/api/adv/carry"
Receive = "https://lambda-treasure-hunt.herokuapp.com/api/adv/receive"
Warp = "https://lambda-treasure-hunt.herokuapp.com/api/adv/warp"
Mine = "https://lambda-treasure-hunt.herokuapp.com/api/adv/mine"
Transmorgify = "https://lambda-treasure-hunt.herokuapp.com/api/transmorgify"
