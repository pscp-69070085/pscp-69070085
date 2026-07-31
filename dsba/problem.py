'''5'''
n = int(input())
a = 0
b = 1
total_sum = 0
i = 0
if n!=1:
    for i in range(n):
        total_sum += a
        next_term = a+b
        a = b
        b = next_term
        i+=1
    print(total_sum)
else:
    print("0")
