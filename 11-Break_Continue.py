# Break Statement
# Terminates the very loop it lies within

for i in range(12):
    print(i)
    if(i==10):
        break


# Continue statement
# Skips the current Iteration

for i in range(12):
    if(i%2==0):
        continue
    print(i)