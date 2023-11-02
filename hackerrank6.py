
def solve(s):
    _list = list(s)
    for i, val in enumerate(_list):
        if i == 0 or _list[i-1] == ' ':
            _list[i] = _list[i].upper()
    result = ''
    for i in _list:
        result += i
    return result

if __name__ == '__main__':
    string = input()
    result = solve(string)
    print(result)
