def maxSubarrayProduct(arr, n):
    max_ = arr[0];
    min_ = arr[0];
    max_so = arr[0];
    
    for i in range(n):
        temp = max({arr[i], arr[i] * max_, arr[i] * min_});
        min_ = min({arr[i], arr[i] * max_, arr[i] * min_});
        max_= temp
        max_so = max(max_so, max_)
    return max_so


arr = [ 1, -2, -3, 0, 7, -8, -2 ]
n = len(arr)
print("Maximum sub-array product is" , maxSubarrayProduct(arr, n))