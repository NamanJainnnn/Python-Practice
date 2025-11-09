for people in range(1,10):
 print(people)

for name in "Naman":
 print (name)

for star in "******":
 print (star)

sun = "*"
num = 1
while num != 5:
 print(sun * num)
 num += 1


sune = "*"
nume = 5
while nume != 0:
 print(sune * nume)
 nume -= 1
#idk for somereason i thought the star problem would come under FOR
#But its of WHile loop! anyways

prices = [10,20,30]
total = 0

for price in prices:
 total += price
 print(f'total: {total}')
 
print("*" * 10)

prices = [10,20,30]
total = 0

for price in prices:
 total += price
 
print(f'total: {total}')
#there is a difference
#if print is inside FOR loop it will show every cycle of sum for the total
#but if its outside it will give u the direct result!

prices = [10,20,30]
total = 0
n = 1
for price in prices:
 total += price
 print(f'Item cycle {n}: {total}')
 n += 1
print('*' * 10)
print(f'Total: {total}')
