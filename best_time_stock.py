# best time too buy and sell stock
prices = [2,1,2,1,0,1,2]

max_price = 0
profit = 0

for i in range(0,len(prices)-1):
    if prices[i] < prices[i+1]:
        print(prices[i])
        print('true')
        for z in range(i, len(prices)):
            if prices[z] > max_price:
                max_price = prices[z]
        print('max price:'+ str(max_price))
        profit = max_price - prices[i]
        print('Profit:'+ str(profit))
        break