# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

if a[0] > a[1]:
    first_max = a[0]
    second_max = a[1]
else:
    first_max = a[1]
    second_max = a[0]

for i in range(2, n):
    if a[i] >= first_max:
        second_max = first_max
        first_max = a[i]
    elif a[i] >= second_max:
        second_max = a[i]

print("first_max: %d | second_max: %d" % (first_max, second_max))
result = first_max * second_max

print(result)