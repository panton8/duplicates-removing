
def remove_duplicates(message):
    symbol_stack = []

    for letter in message:
        if symbol_stack and letter == symbol_stack[-1]:
            symbol_stack.pop()
        else:
            symbol_stack.append(letter)

    return ''.join(symbol_stack)


def main():
    print(remove_duplicates('wwaldaadicffenn'))


if __name__ == '__main__':
    main()
