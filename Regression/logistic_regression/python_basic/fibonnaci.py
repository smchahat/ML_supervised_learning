new_arr = [0, 1]


def fibo(num):
    if num == 0:  
        return 0
    if num == 1:
        return 1
    last = fibo(num-1)
    second_last = fibo(num-2)
    return last + second_last
    


fibo(28)