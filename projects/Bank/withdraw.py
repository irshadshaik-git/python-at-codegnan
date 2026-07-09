#withdraw function defination
from data import user
def withdraw(account:int,withdraw_amount:int)->str:
    curr_amount = user[account]["balance"]
    # check amount
    if curr_amount >=withdraw_amount:
        user[account]["balance"]-=withdraw_amount
        return f"{withdraw_amount} withdrawal successful and  current Balance is {user[account]["balance"]}"
