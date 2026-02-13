for i in range(1_000_000):
    s = str(i).zfill(6)

    left = s[:3]
    right = s[3:]

    if sum(int(c) for c in left) == sum(int(c) for c in right):
        print(s)