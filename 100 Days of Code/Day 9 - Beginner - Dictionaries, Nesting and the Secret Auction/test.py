
biding ={}


def auction(name,bid):
            biding[ur_name] = ur_bid
should_end = False
while not should_end:
    ur_name = input("What is your name?: ")
    ur_bid = input("What's your bid?: ")

    auction(name=ur_name,bid=ur_bid)

    restart =  input("Are there any other bidders? Type 'yes' or 'no'.")
    if restart == "no":
        should_end = True
        print(f"The winner is {max(biding, key=biding.get)} with a bid of ${max(biding.values())}.")

