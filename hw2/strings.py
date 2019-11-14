from typing import List


def filter_lines_of_length_five(lines: List[str]) -> List[str]:
    list_of_five = []
    for string in lines:
        if len(string) == 5:
            list_of_five.append(string)
        else:
            pass
    return list_of_five



if __name__ == '__main__':
    print(filter_lines_of_length_five(['aaa', 'ab', 'abaab', 'ccccc']))