from collections import Counter


def get_coincidences(string, consonant):
    coincidences = {}
    result = {}
    for i in string:
        if consonant:
            if is_consonant(i) and i not in coincidences:
                coincidences[i] = 1
                result = dict(Counter(go_by_thread(i, string, consonant)) +
                    Counter(result))
        else:
            if not is_consonant(i) and i not in coincidences:
                coincidences[i] = 1
                result = dict(Counter(go_by_thread(i, string, consonant)) +
                    Counter(result))
    return result

def go_by_thread(letter, string, consonant):
    coincidences = {}
    storage = letter
    for i in string[string.index(letter)::]:
        if consonant:
            if i == letter and i not in coincidences:
                coincidences[storage] = 0
            elif i != letter and is_consonant(i) and i not in coincidences:
                storage += i
                coincidences[storage] = 0
            elif i == letter and is_consonant(i) and i in coincidences:
                storage += i
                coincidences[storage] = 0
            elif not is_consonant(i) and storage + i not in coincidences:
                storage += i
                coincidences[storage] = 0
            slice_str = string[string.index(storage)::]
            for j, _ in enumerate(slice_str):
                if storage in slice_str[j:j+len(storage)]:
                    coincidences[storage] += 1
        else:
            if i == letter and i not in coincidences:
                coincidences[storage] = 0
            elif i != letter and not is_consonant(i) and i not in coincidences:
                storage += i
                coincidences[storage] = 0
            elif is_consonant(i) and storage + i not in coincidences:
                storage += i
                coincidences[storage] = 0
            elif not is_consonant(i) and storage + i not in coincidences:
                storage += i
                coincidences[storage] = 0
            slice_str = string[string.index(storage)::]
            for j, _ in enumerate(slice_str):
                if storage in slice_str[j:j+len(storage)]:
                    coincidences[storage] += 1
    return coincidences

def is_consonant(letter):
    return letter not in ['A', 'E', 'I', 'O', 'U']


def minion_game(string):
    coincidences = [
        get_coincidences(string, True),
        get_coincidences(string, False)
    ]
    print_winner(coincidences)


def print_winner(coincidences):
    result = [['Stuart', 0], ['Kevin', 0]]
    for index, value in enumerate(coincidences):
        for j in value.items():
            result[index][1] += j[1]
    if result[0][1] > result[1][1]:
        print(result[0][0], result[0][1])
    else:
        print(result[1][0], result[1][1])


if __name__ == '__main__':
    s = input()
    minion_game(s)
