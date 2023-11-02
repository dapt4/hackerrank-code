if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))
    result = hash(t)
    print(result)
