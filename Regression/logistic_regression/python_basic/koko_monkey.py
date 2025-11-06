#leetcode 875

piles = [3,6,7,11]
h = 8

m = max(piles)
total = 0
st = 1
while True:

    mid = (st + m)/2
    for i in piles:
        total += i

    if i > h:
        st = mid
    elif i < h:
        m = mid