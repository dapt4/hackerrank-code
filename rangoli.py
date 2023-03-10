def getLetters(index, letters):
    result = ''
    for i in range(index+1):
        result += letters[i]
    iterable = list(reversed(range(index+1)))
    for i in iterable:
        if i == len(iterable) -1:
            continue
        result += letters[i]
    return result

def print_rangoli(size):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    chars = letters[0:size][::-1]
    line_length = (size + (size-1))*2 -1
    result = ''
    for i in range(len(chars)):
        result += "-".join(getLetters(i, chars)).center(line_length, "-") + "\n"
    chars = chars.replace(chars[len(chars)-1], "")
    for i in reversed(range(len(chars))):
        result += "-".join(getLetters(i, chars)).center(line_length, "-") + "\n"
    print(result)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
