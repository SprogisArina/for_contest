def sort_numbers(n, arr, m, pattern):
    sorted_arr = []
    unsorted_arr = arr.copy()
    for pattern_index in range(m):
        sample = pattern[pattern_index]
        for index in range(n):
            current = unsorted_arr[index]
            if current == sample:
                sorted_arr.append(current)
                arr.remove(current)
    for i in range(1, len(arr)):
        current = arr[i]
        prev = i - 1
        while prev >= 0 and arr[prev] > current:
            arr[prev + 1] = arr[prev]
            prev -= 1
        arr[prev + 1] = current
    sorted_arr.extend(arr)
    return sorted_arr


if __name__ == '__main__':
    with open('input.txt', 'r') as file_in:
        n = int(file_in.readline().rstrip())
        arr = [int(number) for number in (
            file_in.readline().rstrip().split(' '))]
        m = int(file_in.readline().rstrip())
        pattern = [int(number) for number in (
            file_in.readline().rstrip().split(' '))]
    sorted_arr = sort_numbers(n, arr, m, pattern)
    sorted_arr = [str(number) for number in sorted_arr]
    result = str.join(' ', sorted_arr)
    print(str(result))
