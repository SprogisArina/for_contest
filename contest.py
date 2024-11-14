def sort_numbers(n, arr):
    border = 0
    max_number = 0
    for index in range(n):
        max_number = max(max_number, arr[index])
        if index == max_number:
            border += 1
    return border


if __name__ == '__main__':
    with open('input.txt', 'r') as file_in:
        n = int(file_in.readline().rstrip())
        arr = [int(number) for number in (
            file_in.readline().rstrip().split(' '))]
    result = sort_numbers(n, arr)
    print(str(result))
