def count_measurments(number):
    if number == 0 or number == 1:
        return 1
    n = count_measurments(number - 1) + count_measurments(number - 2)
    return n


if __name__ == '__main__':
    with open('input.txt', 'r') as file_in:
        line = file_in.readline().rstrip()
        version = int(line)
    result = count_measurments(version)
    with open('output.txt', 'w') as file_out:
        file_out.write(str(result))
