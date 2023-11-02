
if __name__ == '__main__':
    # n = int(input())
    # arr = list(map(int, input().split()))
    n = 4
    arr = [8,7,6,4,5]
    arr = list(set(arr))
    arr.sort()
    arr = arr[::-1]
    print(arr[1])

