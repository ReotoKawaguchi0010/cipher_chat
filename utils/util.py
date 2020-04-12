import re


def alphabet_check(string):
    alphabet = '[a-zA-Z]'

    for i in string:
        if re.match(alphabet, i) is not None:
            continue
        else:
            return False
            break

    return True


if __name__ == '__main__':

    text = 'sdggファd'
    text2 = 'twat'



    print(alphabet_check(text2))


