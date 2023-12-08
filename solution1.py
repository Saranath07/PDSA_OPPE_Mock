# List A which is completely less than 
# List B

# Swap index 5 

# A = [1, 2, 6, 5, 1, 5]

# B = [3, 4, 3 ,2, 2, 2]

# Swap index 1

# A = [3, 4, 6, 5, 2, 5]

# B = [1, 2, 3 ,2, 1, 2]

def minmax(A, B):

    for i in range(len(A)):
        if B[i] < A[i]:
            A[i], B[i] = B[i], A[i]
    
    return max(A) * max(B)

A = [1, 2, 6, 5, 1, 2]

B = [3, 4, 3 ,2, 2, 5]

print(minmax(A, B))