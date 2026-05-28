from numpy import np

X = np.array([1, 2, 3, 4])

y = np.array([3, 5, 7, 9])

# y = w0 + w1 * X
# x̄ = X.mean()
# ȳ = y.mean()

#w1 =  Σ((x - x̄)(y - ȳ)) / Σ((x - x̄)²)
x_mean = X.mean()
y_mean = y.mean()
w1 = sum((X - x_mean) * (y - y_mean))/ sum((X - x_mean)**2)

#w0 = ȳ - w1x̄
w0 = y_mean - (w1 * x_mean)

# predict for number = 8
num = 8
out = w0 + w1*num

print(f"predicted numbr is {num}")
