from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art

bids = {}
  
def highest_bid(bids):
  highest_bid = 0 
  winner = ""
  for person in bids:
    bid_amount = bids[person]   
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = person
  print(f"The winner of the Silent Auction is {winner} with a bid of ${highest_bid}")

print(art.logo)
print("Welcome to the secret auction program.\n")
reset = True

while reset:
  name = input("What is your name?: ")
  bid_value = int(input("What's your bid?: $"))
  other_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  bids[name] = bid_value
  reset = False
  if other_bidder == 'yes':
    clear()
    reset = True
  elif other_bidder == 'no':
    highest_bid (bids)