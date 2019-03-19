def print_formatted(number):
    result = ''
    for x in range(1, number+1):
        octagonal = oct(x).replace('0o', '')
        hexadecimal = hex(x).replace('0x', '').upper()
        binary = bin(x).replace('0b', '')
        if x != number:
            result += '{} {} {} {}'.format(x, octagonal, hexadecimal, binary) + '\n'
        else:
            result += '{} {} {} {}'.format(x, octagonal, hexadecimal, binary)
    return print(result)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
