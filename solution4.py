def peak_unimodal(A):
    low = 0
    high = len(A) - 1
    while (high - low) >= 0:
        mid = (low + high) // 2
        if A[mid - 1] < A[mid] > A[mid + 1]:
            return mid 
        
        if A[mid] < A[mid + 1]:
            low = mid + 1
        
        else:
            high = mid - 1
    
    return "This list is not unimodal"


A = list(map(int, '2 3 4 21 43 52 51 18 11 9 6 5 1'.split()))
print(peak_unimodal(A))