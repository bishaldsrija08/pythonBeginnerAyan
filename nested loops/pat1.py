"""
1
1 2
1 2 3
1 2 3 4
"""

line =4
for i in range(1, line+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print() # New line after inner loop
    

# i = 1, j=1 =>1
# i = 2, j=1 =>1 2
# i = 3, j=1 =>1 2 3
# i = 4, j=1 =>1 2 3 4



"""
*
* *
* * *
* * * *
"""

line = 4
for i in range(1, line+1):
    for j in range(1, i+1):
        print('*', end=' ')
    print() # New line after inner loop
    
"""
C
C H
C H I
C H I T
C H I T A
C H I T A W
C H I T A W A N
"""

line = 7
word = "CHITAWAN"
for i in range(1, line+1):
    for j in range(0, i+1):
        print(word[j], end=' ')
    print() # New line after inner loop
    


"""
* * * * *
* * * *
* * *
* *
*
"""

line = 5
for i in range(line, 0, -1):
    for j in range(1, i+1):
        print('*', end=' ')
    print() # New line after inner loop