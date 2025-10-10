import time

loan = {}

def payment_made(amt : int):
    curr = int(time.time())
    if curr in loan:
        loan[curr] += amt
    else:
        loan[curr] = amt


def loan_given():
    total_amt = 0
    curr = int(time.time())
    last_hour = curr - 3600

    for keys in loan:
        if keys <= curr and keys > last_hour:
            total_amt += loan[keys]

    return total_amt

payment_made(5200)
payment_made(50)

print(loan_given())
