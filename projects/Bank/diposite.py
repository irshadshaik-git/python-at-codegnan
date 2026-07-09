#diposite function Defination
from data import user
def deposite(account:int,deposite_amount:int):
    curr_amount = user[account]["balance"]
    # check amount
    user[account]["balance"]+=deposite_amount
    return f"{deposite_amount} withdrawal successful and current Balance is {user[account]["balance"]}"