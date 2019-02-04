def split_and_join(line):
    nline = line.split(" ")
    return '-'.join(nline)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
