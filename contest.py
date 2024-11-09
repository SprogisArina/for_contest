def comparison(line):
    substring = ''
    max_len = 0
    for symbol in line:
        if symbol in substring:
            index = substring.find(symbol)
            seq = substring[:(index + 1)]
            substring = substring.lstrip(seq)
            substring += symbol
        else:
            substring += symbol
            substring_len = len(substring)
            max_len = max(max_len, substring_len)
    return max_len


if __name__ == '__main__':
    with open('input.txt', 'r') as file_in:
        line = file_in.readline().rstrip()
    result = comparison(line)
    with open('output.txt', 'w') as file_out:
        file_out.write(str(result))
