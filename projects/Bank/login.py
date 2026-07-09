from data import user
def login(account:int,password:str)->bool:
    #check accpount exists in user or not
    if account in user:
        if password == user[account]["password"]:
            return True
        return False
    return False