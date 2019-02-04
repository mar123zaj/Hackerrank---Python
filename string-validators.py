def check_properties(word):
    alnum = alpha = digit = upper = lower = False
    for letter in word:
        if letter.isalnum():
            alnum = True
        if letter.isalpha():
            alpha = True
        if letter.isdigit():
            digit = True
        if letter.islower():
            lower = True
        if letter.isupper():
            upper = True

    return "%r\n%r\n%r\n%r\n%r" % (alnum, alpha, digit, lower, upper)

if __name__ == '__main__':
    s = input()
    print(check_properties(s))
