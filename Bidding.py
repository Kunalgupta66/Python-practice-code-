def find_bidder(bidding_dictionary):
    winner = ""
    higher_bid = 0 

    max(bidding_dictionary)

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > higher_bid:
            higher_bid = bid_amount
            winner = bidder
    
    print(f"The winner is {winner} with a bid of ${higher_bid}.")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_contine = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_contine == 'no':
        continue_bidding = False
        find_bidder(bids)
    elif should_contine == 'yes':
        print("\n" * 20)