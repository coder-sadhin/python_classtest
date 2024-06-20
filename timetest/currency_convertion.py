def usd_to_rmb(usd_amount):
    exchange_rate = 7.0263
    rmb_amount = usd_amount * exchange_rate
    print(f"￥{rmb_amount:.2f} Yuan")

def rmb_to_usd(rmb_amount):
    exchange_rate = 7.0263
    usd_amount = rmb_amount / exchange_rate
    print(f"${usd_amount:.2f} Dollar")

def which_one(v):
    if v[0] == "￥":
        rmb_amount = float(v[1:])
        rmb_to_usd(rmb_amount)
    elif v[0] == "$":
        usd_amount = float(v[1:])
        usd_to_rmb(usd_amount)
    else:
        print("Invalid currency symbol provided")


which_one(input())