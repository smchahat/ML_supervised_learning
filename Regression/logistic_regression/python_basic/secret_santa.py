

import pandas as pd
import random

file = pd.read_csv('C:/Users/chaha/Downloads/customers-100.csv')

f = file["Email"]
l = list(f)

emails = l[:4]
givers = emails[:]

while True:
    random.shuffle(givers)
    flag = 0
    for z,a in zip(emails, givers):
        if z == a:
            flag = 1

    if flag == 0:
        break
    
    
for a,b in zip(emails, givers):
    print(a, " gives to ", b)
