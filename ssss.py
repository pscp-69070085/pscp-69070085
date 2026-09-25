n = int(input())

temp = n
base = 0

if temp > 200:
    base += (temp - 200) * 15
    temp = 200
if temp > 100:
    base += (temp - 100) * 12
    temp = 100
if temp > 50:
    base += (temp - 50) * 10
    temp = 50
if temp > 10:
    base += (temp - 10) * 7
    temp = 10
if temp > 0:
    base += temp * 5

total = base + (n * 0.50) + (base * 0.07)
print(f"{total:.1f}")