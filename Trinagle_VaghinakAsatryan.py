n = 5

i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end = " ")
        j += 1
    print()
    i += 1

print("_______________________________________________________")

n = 1

i = 5
while i >= n:
    j = 1
    while j <= i:
        print("*", end = " ")
        j += 1
    print()
    i -= 1

print("_______________________________________________________")

rows = 5
i = 1
while i <= rows:
    j = i
    while j < rows:
        print(' ', end=' ')
        j += 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i += 1

print("_______________________________________________________")

rows = 5
i = rows
while i >= 1:
    j = rows
    while j > i:
        print(' ', end=' ')
        j -= 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i -= 1

print("______________________________________________________________")

rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")

k = rows - 2

for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")

#Comment