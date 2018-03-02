def shift(letter, shift_amount):
    unicode_value = ord(letter) + shift_amount
    
    if unicode_value > 126:
        new_shift = unicode_value - 126
        position = 31 + new_shift
        new_letter = chr(position)
        
    elif unicode_value < 32:
        new_shift = 32 - unicode_value
        position = 127 - new_shift
        new_letter = chr(position)
        
    else:
        new_letter = chr(unicode_value)
    return new_letter

def encrypt(message, shift_amount):
    result = ""
    for letter in message:
        result += shift(letter, shift_amount)

    return result


def decrypt(message, shift_amount):
    result = ""
    for letter in message:
        result += shift(letter, -1 *shift_amount)

    return result

with open("text_files/file_001597.txt", 'r') as f:
    secret_message = f.read()
    
decrypted_message = decrypt(secret_message, 34)
print(decrypted_message)
