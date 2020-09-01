def reverse(arr, s, e):
    while e > s:
        temp = arr[s]
        arr[s] = arr[e]
        arr[e] = temp
        e -= 1
        s += 1
    return arr


def left_rotate(d, arr):
    d = d % len(arr)
    reverse(arr, 0, d - 1)

    reverse(arr, d, len(arr) - 1)
    reverse(arr, 0, len(arr) - 1)
    return arr


def right_rotate(d, arr):
    d = d%len(arr)
    reverse(arr, 0, len(arr) - d - 1)
    reverse(arr, len(arr) - d, len(arr) - 1)
    reverse(arr, 0, len(arr) - 1)
    return arr


print(left_rotate(2, [1, 2, 3, 4, 5, 6, 7]))
print(right_rotate(3, [1, 2, 3, 4, 5, 6, 7]))


# finding the pivot
def pivot(arr, lo, hi):
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] > arr[mid + 1] and hi > mid:
            return [mid]
        elif arr[mid - 1] > arr[mid] and mid > lo:
            return [mid - 1]
        if arr[mid] <= arr[lo]:
            hi = mid - 1
        else:
            lo = mid + 1


print(pivot(right_rotate(3, [1, 2, 3, 4, 5, 6, 7]), 0, 7))

# print an element after K rotations
def ithelement(arr,d,k):
    for i in range(len(arr)):
        if arr[i]==k:break
    k = (len(arr) - d - i)%len(arr)
    if k<0: k = len(arr)+k
    return k
print(left_rotate(7,[1,2,3,4,5,6]))
print(ithelement([1,2,3,4,5,6],7,4))