s = 'Hello Python'
i = 0
for _ in s:
    print(' '*i + s[:i+1])
    i += 1
i = len(s)-2
for _ in s:
    print(' '*i + s[:i+1])
    i -= 1