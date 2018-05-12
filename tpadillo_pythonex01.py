## How much is your total bill? 150
## How much is your payment? 200
## Hi! Your change is 50.00



print('How much is your total bill?: ')
total_bill = float(input())
print('How much is your payment?: ')
payment = float(input())

change = float(payment - total_bill)
print('Hi! Your change is ' + str(change))

##print(type(change))
