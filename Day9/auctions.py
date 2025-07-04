import gavel

bidders = {}
continue_bidding = False

print(gavel.gavel_art)

def highest_bidder(bidder_dictionary):
    highest_bid = 0
    winner = ""

    for bidder in bidder_dictionary:
        bid_amount = bidder_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")



while not continue_bidding:
    name = input("What is your name ?\n")
    bid_price = int(input("What is your bid amount ?\n"))

    bidders[name] = bid_price

    wish_to_continue = input("Are there any more bidders ? Type 'yes' or 'no'\n").lower()

    if wish_to_continue == 'no':
        continue_bidding = True
        highest_bidder(bidders)
    elif wish_to_continue == "yes":
        print("\n" * 1000)





