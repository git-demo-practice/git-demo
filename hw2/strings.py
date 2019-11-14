from typing import List


def filter_lines_of_length_five(lines: List[str]) -> List[str]:
    return list(filter(lambda line: len(line) == 5, lines))


if __name__ == '__main__':
    print(filter_lines_of_length_five(['aaa', 'ab', 'abaab', 'ccccc']))