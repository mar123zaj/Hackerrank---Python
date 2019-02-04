# Enter your code here. Read input from STDIN. Print output to STDOUT
user_input = input()
numbers = user_input.split()
n = int(numbers[0])
m = int(numbers[1])
if n % 2 != 0 and m == n*3:
    new_n = int((n-1)/2)
    new_pattern = '.|.'
    for x in range(new_n):
        if x != 0:
            new_pattern = '.|.' + new_pattern + '.|.'
        print(new_pattern.center(m, '-'))
    print('WELCOME'.center(m, '-'))
    for x in range(0, new_n*3, 3):
        if x != len(new_pattern)-x:
            print(new_pattern[0 + x:len(new_pattern) - x].center(m, '-'))
