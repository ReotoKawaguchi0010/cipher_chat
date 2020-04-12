from utils import cipher


def order_cipher(text, *args):
    shift = cipher.ShiftCipher()
    scytale = cipher.ScytaleCipher()
    if args[0] == 'shift':
        first = shift.shift_letters_encode(text, 3)
    elif args[0] == 'scytale':
        first = scytale.scytale_letters_encode(text, 5)

    if args[1] == 'shift':
        return shift.shift_letters_encode(first, 3)
    elif args[1] == 'scytale':
        return scytale.scytale_letters_encode(first, 5)





if __name__ == '__main__':
    t = order_cipher('hello', 'shift', 'scytale')
    print(t)