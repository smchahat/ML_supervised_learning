word1 = "ab"
word2 = "pqrs"

length_str1 = len(word1) 
length_str2 = len(word2)

length = min(length_str1, length_str2)

print(length)
output = ""

for i in range(length):
    output = output + word1[i] + word2[i]

if length_str1 > length_str2:
    output = output + word1[length:]
else: 
    output = output + word2[length:]
print(output)