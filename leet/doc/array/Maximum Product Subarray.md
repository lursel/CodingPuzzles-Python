# Problem

http://www.lintcode.com/en/problem/maximum-product-subarray/

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

*Example*

For example, given the array ```[2,3,-2,4]```, the contiguous subarray ```[2,3]``` has the largest product = ```6```.

# Thoughts

# My Solution

```
def maxProduct(A):
    if len(A) == 0:
        return 0
        
    min_tmp = A[0]
    max_tmp = A[0]
    result = A[0]
    for i in range(1, len(A)):
        a = A[i] * min_tmp
        b = A[i] * max_tmp
        c = A[i]
        max_tmp = max(max(a, b), c)
        min_tmp = min(min(a, b), c)
        result = max_tmp if max_tmp > result else result
    return result
```