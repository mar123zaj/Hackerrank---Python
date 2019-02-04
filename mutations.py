def mutate_string(string, position, character):
    string_list = list(string)
    del string_list[position]
    string_list = ''.join(string_list)
    string_list = string_list[:position] + character + string_list[position:]
    return string_list

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)