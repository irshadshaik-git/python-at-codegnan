#transfer function defination
from data import user

def transfer(sender:int,receiver:int,transfer_amount:int):
    if receiver in user:
        curr_amount = user[sender]["balance"]
        if curr_amount >= transfer_amount:
            user[sender]["balance"]-=transfer_amount
            user[receiver]["balance"]+=transfer_amount
            return f"{transfer_amount} withdrawal successful and current Balance is {user[sender]["balance"]}"
        return"insufficient Balance"
    return "Reciever account not Found"
