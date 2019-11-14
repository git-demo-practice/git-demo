from typing import List


def filter_lines_of_length_five(lines: List[str]) -> List[str]:
    res = []
    for lin in lines:
        if len(lin) == 5:
            res.append(lin)
    return res


if __name__ == '__main__':
    print(filter_lines_of_length_five(['aaa', 'ab', 'abaab', 'ccccc']))