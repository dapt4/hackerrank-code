

def count_chars(string):
    count = {}
    for i in string:
        if i not in count:
            count[i] = 1
        elif i in count:
            count[i] += 1
    return count


def print_results(_list):
    for i in range(3):
        print(_list[i][0], _list[i][1])


def main(s):
    sort = ''.join(sorted(s))
    count = count_chars(sort)
    sorted_counts = sorted(count.items(), reverse=True, key=lambda item: item[1])
    print_results(sorted_counts)


if __name__ == '__main__':
    s = input()
    main(s)

