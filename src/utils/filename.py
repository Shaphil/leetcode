def get_filename(text: str) -> str:
    punctuations = ['.', ',']
    empty = ''

    # remove punctuations
    for p in punctuations:
        text = text.replace(p, empty)

    space = ' '
    dash = '-'
    under = '_'

    # replace spaces and dashes with underscores
    text = text.replace(space, under)
    text = text.replace(dash, under)

    # lowercase text
    text = text.lower()

    return text


def main():
    original_name = input('Please insert the problem name: ')
    filename = get_filename(original_name)
    print('\x1b[0;34m' + filename + '\x1b[0m')


if __name__ == '__main__':
    main()
