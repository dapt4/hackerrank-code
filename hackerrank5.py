def wrap(string, max_width):
    slices = []
    accumulated = 0
    while accumulated < len(string):
        splited = string[accumulated:accumulated + max_width:]
        slices.append(splited)
        accumulated += max_width
    result = ''
    for i in slices:
        result += i + '\n'
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
