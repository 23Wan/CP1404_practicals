num = int(input('Number of items: '))
total = 0.0
for prices in range (num):
 total += float(input('Price of item: '))
if total > 100:
 total = total - (total * 0.1)
print('Total price of three items ', "${:,.2f}".format(total))