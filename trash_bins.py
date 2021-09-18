t = int(input())

def closest_bin(index, street):
    closest_left = len(street)
    closest_right = len(street)
    for i in range(index, len(street)):
        if (street[i] == "1"):
            closest_right = abs(index - i)
            break
    for i in range(index, -1, -1):
        if (street[i] == "1"):
            closest_left = abs(index - i)
            break
    return min(closest_left, closest_right)

for x in range(0, t):
    length = int(input())
    street = list(input())
    result = 0
    for index, bin in enumerate(street):
        if (bin == "0"):
            result += closest_bin(index, street)
    print(f"Case #{x+1}: {result}")
