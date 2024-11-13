def count(applicant_number, cycles):
    applicants = [applicant + 1 for applicant in range(applicant_number)]
    retired = 0
    while applicant_number > 0:
        retired = (retired + cycles - 1) % applicant_number
        winner = applicants.pop(retired)
        applicant_number -= 1
    return winner


if __name__ == '__main__':
    with open('input.txt', 'r') as file_in:
        number, cycles = (int(file_in.readline().rstrip()) for _ in range(2))
    result = count(number, cycles)
    with open('output.txt', 'w') as file_out:
        file_out.write(str(result))
