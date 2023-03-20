print('a')
for i in range(1, 21, 2):
    print(i, end=' ')
print('\n','b')
num = 20
while num > 0:
   print(num)
   num=num-1
print(num,end='\r')
print('c')
num_starts = int (input('number of stars :'))
for output in  range (num_starts):
    print("*",end= "")
print('\n','d.')
rows = int(input("enter the number of row:"))
stars =1
for lines in range (0,rows):
    for result in  range (0,stars):
     print("*",end="")
stars=stars+1
print()