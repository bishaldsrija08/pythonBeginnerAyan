line = 5
for i in range(line, 0, -1):
    for j in range(1, i+1):
        print('*', end=' ')
    print() # New line after inner loop