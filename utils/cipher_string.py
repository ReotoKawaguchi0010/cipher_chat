import string


lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
for_lowercase = string.ascii_lowercase + string.ascii_lowercase
for_uppercase = string.ascii_uppercase + string.ascii_uppercase


class EnigmaString(object):

    def __init__(self):
        dictionary = {
            0 : 'a',
            1 : 'b',
            2 : 'c',
            3 : 'd',
            4 : 'e',
            5 : 'f',
            6 : 'g',
            7 : 'h',
            8 : 'i',
            9 : 'j',
            10 : 'k',
            11 : 'l',
            12 : 'm',
            13 : 'n',
            14 : 'o',
            15 : 'p',
            16 : 'q',
            17 : 'r',
            18 : 's',
            19 : 't',
            20 : 'u',
            21 : 'v',
            22 : 'w',
            23 : 'x',
            24 : 'y',
            25 : 'z'
        }

if __name__ == '__main__':
    enigma = EnigmaString()

    list_a = [0, 1, 2, 3, 0, 1, 2, 3]




    a = {for_lowercase[0] : for_lowercase[list_a[0-1]],
         for_lowercase[1] : for_lowercase[list_a[1-1]],
         for_lowercase[2] : for_lowercase[list_a[2-1]],
         for_lowercase[3] : for_lowercase[list_a[3-1]]}

    A = {for_lowercase[0] : for_lowercase[3],
         for_lowercase[1] : for_lowercase[0],
         for_lowercase[2] : for_lowercase[2],
         for_lowercase[3] : for_lowercase[1]}

    b = {for_lowercase[0]: for_lowercase[list_a[0+1]],
         for_lowercase[1]: for_lowercase[list_a[1+1]],
         for_lowercase[2]: for_lowercase[list_a[2+1]],
         for_lowercase[3]: for_lowercase[list_a[3+1]]}


    print(b['a'])


