# List A which is completely less than 
# List B

# Swap index 5 

# A = [1, 2, 6, 5, 1, 2]

# B = [3, 4, 3 ,2, 2, 5]

# Swap index 1

# A = [3, 4, 6, 5, 2, 5]

# B = [1, 2, 3 ,2, 1, 2]

def minmax(A, B):
    if len(A) < len(B):
        X = A
        Y = B
    else:
        X = B
        Y = A
    for i in range(len(X)):
        if Y[i] < X[i]:
            X[i], Y[i] = Y[i], X[i]
    
    return max(X) * max(Y)

A = [1, 2, 6, 5, 1, 2, 7]

B = [3, 4, 3 ,2, 2, 5]

print(minmax(A, B))

