if __name__ == '__main__':
    my_list = []
    N = int(input("Please give me number of actions that you would like to do: "))
    commands = ['insert', 'remove', 'append', 'sort', 'reverse', 'pop']
    for n in range(N):
        my_input = input("Use: insert, print, remove, append, sort, pop or reverse on your list ").split(' ')
        if my_input[0] in commands:
            command = my_input[0]
            arguments = my_input[1:]
            new_arguments = ', '.join(arguments)
            eval('my_list.' + command + '(' + new_arguments + ')')
        elif my_input[0] == 'print':
            print(my_list)
        else:
            print("It wasn't valid command!")

