
def remove_duplicates(message):
    symbol_stack = []

    for letter in message:
        if symbol_stack and letter == symbol_stack[-1]:
            symbol_stack.pop()
        else:
            symbol_stack.append(letter)

    return ''.join(symbol_stack)


def main():
    with open('data.txt', 'r') as file:
        data = file.read()
        res = remove_duplicates(data)
        print(res)
        res_file = open("result.txt", "w+")
        res_file.write(res)
        res_file.close()


if __name__ == '__main__':
    main()
