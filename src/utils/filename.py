from string import punctuation


def get_filename(text: str) -> str:
    punctuations = ['.', ',']
    empty = ''

    # remove punctuations
    for p in punctuations:
        text = text.replace(p, empty)

    space = ' '
    under = '_'

    # replace spaces with underscores
    text = text.replace(space, under)

    # lowercase text
    text = text.lower()

    return text


def main():
    original_name = '844. Backspace String Compare'
    filename = get_filename(original_name)
    print(filename)


if __name__ == '__main__':
    main()
