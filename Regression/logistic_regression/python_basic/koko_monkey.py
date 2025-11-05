#leetcode 875

piles = [3,6,7,11]
h = 8

m = max(piles)
total = 0

while True:

    for i in piles:
        total += i

    if i > h:
        