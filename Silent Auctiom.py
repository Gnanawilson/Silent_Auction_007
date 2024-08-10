import os
def find_winner(bidder_details):
    high_bid=0
    winner=""
    for bidder in bidder_details:#wils:10000,sel:20000,roo:30000
        bidding_prize=bidder_details[bidder] 
        if bidding_prize>high_bid:
            high_bid=bidding_prize
            winner=bidder
    print(bidder_details)        
    print(f" the winnner is {winner}🏆 with bid prize of{high_bid}")    
             
    
bidder_data={}
end_bidding=False
while not end_bidding:
   name=input("What is your name?: ")
   prize=int(input("What is your bid?: "))
   bidder_data[name]=prize
   more_bidders=input("Are there more bidders? Type 'yes' or 'no' : ").lower()
   if more_bidders=='no':
       end_bidding=True
       find_winner(bidder_data) 
   elif more_bidders=='yes':
       os.system('cls')