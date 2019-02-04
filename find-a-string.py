def count_substring(string, sub_string):
    count = 0
    length = len(string)
    sub_length = len(sub_string)
    for iteration in range(length-sub_length+1):
        if string[iteration:sub_length+iteration] == sub_string:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
