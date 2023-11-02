def solve(val):
    try:
        _list = val.split(' ')
        a, b = int(_list[0]), int(_list[1])
        result = a // b
        print(result)
    except (ZeroDivisionError, ValueError) as err:
        print("Error Code:", err)

if __name__ == '__main__':
        n = int(input())
        for i in range(n):
            val = input()
            solve(val)
