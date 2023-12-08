# Swapping Min-max

You are given two lists a and b of n positive integers each. You can apply the following swap operation to them any r times:
Select index $i \ (0 ≤ i ≤ n − 1)$ and swap $a$; with $b$; (i.e. a; becomes b; and vice versa).
Write a function `minmax(a,b)` which takes two lists a and b of size n as inputs and returns an integer, which is the mini possible value of $max(a_0, a_1, ..., a_{n−1}) \times max(b_0, b_1,..., b_{n-1})$ you can get after applying the swap operation any n times (possibly zero).
Example

Consider the lists - `a = [1,2,6,5,1,2]` and `b = [3,4,3,2,2,5]`

In this case, you can apply the swap operation at indices 1 and 5, then  

`max(1, 4, 6, 5, 1, 5) × max (3, 2, 3, 2, 2, 2) = 6 × 3 = 18`

## Sample Input 1

```
1 2 6 5 1 2
3 4 3 2 2 5
```
## Output

```
18
```

## Sample Input 2

```
3 3 3
3 3 3
```
## Output

```
19
```