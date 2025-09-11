bubble = [5, 4, 1, 2, 3]

for i in range(len(bubble)):
    for j in range( len(bubble)):
        if bubble[i] < bubble[j]:
            bubble[i], bubble[j] = bubble[j], bubble[i]

print(bubble)