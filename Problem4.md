# Peak in Unimodal

Consider an list A with n entries, with each entry holding a distinct number. The sequence of values `A[0], A[1], . . . , A[n-1]` is unimodal: For some index `p` between $0$ and $n - 1 $, the values in the array entries increase up to position `p` in `A` and then decrease the remainder of the way until position $n-1$. (Assume length of A is at least 3)

Write a function peak_unimodal, that takes a list A as input and returns the index of the peak in A in $O(\log n)$ time

## Sample Input 1

```
2 3 4 21 43 52 51 18 11 9 6 5 1 
```

## Output

```
5
```

## Sample Input 2
```
8 9 3
```

## Output
```
1
```