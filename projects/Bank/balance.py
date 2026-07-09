#balance function defination
from data import user
def balance(account:int)->int:
    curr_amount = user[account]["balance"]
    return curr_amount