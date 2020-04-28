from utils import cipher


def order_cipher(text, *args):
    shift = cipher.ShiftCipher()
    scytale = cipher.ScytaleCipher()
    r_text = [text]
    for i in range(len(args)):
        if args[i] == 'shift':
            r_text.append(shift.shift_letters_encode(r_text[i], 3))
        elif args[i] == 'scytale':
            print(r_text[i])
            r_text.append(scytale.scytale_letters_encode(r_text[i], 5))
    return r_text



if __name__ == '__main__':
    print(order_cipher('a', 'shift', 'scytale', 'scytale', 'scytale'))
    print(bin(9))
    print(bin(ord('ア')))
    print(int(bin(ord('/')), 2))