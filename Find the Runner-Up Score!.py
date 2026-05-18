n = int(input())

arr = list(map(int, input().split()))

arr.sort()

highest = arr[-1]

for i in range(n-1, -1, -1):

    if arr[i] != highest:
        print(arr[i])
        break

    