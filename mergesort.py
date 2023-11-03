"""l=123
temp=l
ans=0

while(temp>0):
    re=temp%10
    ans=ans*10+re
    temp=temp//10

print(ans)
#length of string using recursion
sum=1
def callen(Str):
    if(Str==""):
        return 0
    return sum+callen(Str[1:])
    



Str="ajaywww"
count=0
print(callen(Str))"""





#mergesorttt

def merge(arr, low, mid, high):
    temp = []  # temporary array
    left = low  # starting index of left half of arr
    right = mid + 1  # starting index of right half of arr

    # storing elements in the temporary array in a sorted manner
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # if elements on the left half are still left
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # if elements on the right half are still left
    while right <= high:
        temp.append(arr[right])
        right += 1

    # transferring all elements from temporary to arr
    for i in range(low, high + 1):
        arr[i] = temp[i - low]


def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)  # left half
    merge_sort(arr, mid + 1, high)  # right half
    merge(arr, low, mid, high)  # merging sorted halves


if __name__ == "__main__":
    n = 7
    arr = [9, 4, 7, 6, 3, 1, 5]
    print("Before sorting array:")
    print(*arr)

    merge_sort(arr, 0, n - 1)

    print("After sorting array:")
    print(*arr)
