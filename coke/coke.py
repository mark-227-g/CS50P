###################
# CS50P Python
# Mark Edwards
# Lesson 1
##################
cost=50
paid=0
while True:
    print("Amount Due: ", cost-paid)
    coin = int(input("Insert Coin: "))
    if(coin in [5,10,25]):
        paid += coin
        if(paid >= cost):
             break
print("Change Due: ", str(paid-cost))


