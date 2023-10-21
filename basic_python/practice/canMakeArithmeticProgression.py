def canMakeArithmeticProgression(arr):
    arr.sort()
    interval = arr[1] - arr[0]
    for i in range(1, len(arr)-1):
        if arr[i+1] - arr[i] != interval:
            return False
    return True


print(canMakeArithmeticProgression([3,2,1,4]))