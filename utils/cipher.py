import string
import random


class Cipher(object):

    def __init__(self):
        self.encode_text_input = ''
        self.decode_text_input = ''
        self.space = ' '

    def rondom_name(self, append_letter_num):
        results = [random.choice(string.ascii_letters + string.digits) for i in range(append_letter_num)]
        return ''.join(results)

class ShiftCipher(Cipher):

    def shift_letter_encode(self, encode_text_input, num, shift_num):
        i = 0
        while True:
            if encode_text_input[num] == string.ascii_letters[i]:
                encoded_letter = string.ascii_letters[i + shift_num]
                i = 0
                break
            elif encode_text_input[num] == ' ':
                encoded_letter = encode_text_input[num].replace(' ', ' ')
                break
            i += 1
        return encoded_letter

    def shift_letters_encode(self, encode_text_input, shift_num):
        text_list = []
        if encode_text_input is None:
            print('この入力は無効です')
        else:
            for j in range(len(encode_text_input)):
                text_list.append(self.shift_letter_encode(encode_text_input , j, shift_num))
        result = ''.join(text_list)
        return result


class ScytaleCipher(Cipher):

    def scytale_letter_encode(self, encode_text_input, num, append_letter_num):
        i = 0
        while True:
            if encode_text_input[num] == string.ascii_letters[i]:
                encoded_letter = string.ascii_letters[i]
                i = 0
                break
            elif encode_text_input[num] == ' ':
                encoded_letter = encode_text_input[num].replace(' ', '.')
                break
            i += 1
        return encoded_letter + self.rondom_name(append_letter_num)

    def scytale_letters_encode(self, encode_text_input, append_letter_num):
        text_list = []
        if encode_text_input is None:
            print('この入力は無効です')
        else:
            for j in range(len(encode_text_input)):
                text_list.append(self.scytale_letter_encode(encode_text_input, j, append_letter_num))
        result = ''.join(text_list)
        return result

    def scytale_letters_decode(self, decode_letter_num):
        decode_text = []
        i = 0
        while True:
            if i >= len(self.decode_text_input):
                break
            decode_text.append(self.decode_text_input[i])
            i += decode_letter_num + 1
        result = ''.join(decode_text)
        result = result.replace('.', ' ')
        return result



if __name__ == '__main__':

    cipher = ShiftCipher()
    test = cipher.shift_letters_encode('te st', 3)
    print(test)



