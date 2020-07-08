n = str(input("Введите число."))
i = 0
c = 0
while i < len(n):
    x = int(n[i])
    if c < x:
        c = x
    i += 1
print(c)