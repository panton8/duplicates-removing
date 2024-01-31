import sys


def remove_duplicates(message):
    symbol_stack = []

    for letter in message:
        if symbol_stack and letter == symbol_stack[-1]:
            symbol_stack.pop()
        else:
            symbol_stack.append(letter)

    return ''.join(symbol_stack)


def main():
    if len(sys.argv) != 2:
        print("Correct usage example: python alice.py path/to/file.txt")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r') as file:
            data = file.read()
            res = remove_duplicates(data)
            print(res)
            res_file = open("result.txt", "w+")
            res_file.write(res)
            res_file.close()

    except FileNotFoundError:
        print(f"File not found: {file_path}. Choose correct path to file.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
