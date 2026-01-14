import os
print("******Welcome to the Silent Auction Program******")
def winner(bidder_details):
    highest_bid=0
    winner=""
    for bidder in bidder_details:
       bidding_price=bidder_details[bidder]
       if bidding_price>highest_bid:
            highest_bid=bidding_price
            winner=bidder
    print(f"Here is a list of all the bidders:{bidder_details}")
    print(f"The winner is {winner} with the bid price of {highest_bid}")
bidder_data={}
end_of_bidding=False
while not end_of_bidding:
    name=input("What is your name?:")
    bid=int(input("Enter your bid:"))
    bidder_data[name]=bid
    more_bidders=input("Are their more bidders? Type 'yes' or 'no':").lower()
    if more_bidders=='no':
        end_of_bidding=True
        winner(bidder_data)
    elif more_bidders=='yes':
        os.system('cls')
