def sort_values(arr):
    return arr[1]

if __name__ == '__main__':
    '''nested = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested.append([name, score])'''
    nested = [['Harsh',20],['Beria', 20], ['Varun', 19], ['Kakunami', 19], ['Vilkas', 21]]
    nested.sort(key=sort_values)
    print(nested)
    second_lowest: list
    second_lowest_index: int
    for index, key in enumerate(nested):
        if key[1] > nested[0][1]:
            second_lowest = key
            second_lowest_index = index
            break
    repeat = [second_lowest]
    for index, key in enumerate(nested):
        if index == second_lowest_index:
            continue
        if second_lowest[1] == key[1]:
            repeat.append(key)
    repeat.sort()
    for key in repeat:
        print(key[0])
