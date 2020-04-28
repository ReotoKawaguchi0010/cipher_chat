import string
import random
import hashlib


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
        if '/ja/' in encode_text_input :
            text_list.append('/ja/')
            encode_text_input = encode_text_input.replace('/ja/', '')

        try:
            for j in range(len(encode_text_input)):
                text_list.append(self.shift_letter_encode(encode_text_input , j, shift_num))
            result = ''.join(text_list)
            return result
        except:
            return encode_text_input


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

        if '/ja/' in encode_text_input :
            text_list.append('/ja/')
            encode_text_input = encode_text_input.replace('/ja/', '')
        try:
            for j in range(len(encode_text_input)):
                text_list.append(self.scytale_letter_encode(encode_text_input, j, append_letter_num))
            result = ''.join(text_list)
            return result
        except:
            return encode_text_input

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


class BinCipher():

    def bin_letter(self, letter):
        bin_text = []
        for i in range(len(letter)):
            text = bin(ord(letter[i]))
            bin_text.append(text)
        bin_letter = ''.join(bin_text)
        bin_letter_comma =  bin_letter.replace('0b', ',')
        bin_letter_comma = bin_letter_comma[0].replace(',', '') + bin_letter_comma[1:]
        return bin_letter_comma

    def encode(self, letter, password):
        bin_text = str(self.bin_letter(letter))
        bin_password = str(self.bin_letter(password))

        result = bin_text + ',' + bin_password
        return result

    def decode(self, encode_text):
        decode = self.remove_comma(encode_text)
        result = []
        for i in decode:
            hex = int(i, 2)
            result.append(chr(hex))
        return ''.join(result)

    def remove_comma(self, in_comma):
        result = []
        init = []
        for i in in_comma:
            if i == ',':
                last = ''.join(init)
                result.append(last)
                init = []
                continue
            init.append(i)
        last = ''.join(init)
        result.append(last)
        return result



if __name__ == '__main__':

    bin_cipher = BinCipher()
    t = bin_cipher.encode('test', 'pass')

    print(t)
