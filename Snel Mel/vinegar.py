alphabet = "abcdefghijklmnopqrstuvwxyz"

def vinegar_encrypt(text, keyword):
    encryption = ""
    repeats = len(text)//len(keyword)
    remainder = len(text) % len(keyword)
    key = keyword * repeats
    for i in range(remainder):
        letter = keyword[i]
        key += letter
    for i in range(len(text)):
        t = text[i].lower()
        t_place = alphabet.find(t)
        k = key[i].lower()
        k_place = alphabet.find(k)
        shift = k_place
        if t not in alphabet:
            encryption += text[i]
        else:
            if t_place + shift >= len(alphabet):
                new_value = t_place + shift - len(alphabet)
            else:
                new_value = t_place + shift
            encryption += chr(new_value + 97)
    print(text)
    print(key)
    print(encryption)

def vinegar_decrypt(text, keyword):
    decryption = ""
    repeats = len(text)//len(keyword)
    remainder = len(text) % len(keyword)
    key = keyword * repeats
    for i in range(remainder):
        letter = keyword[i]
        key += letter
    for i in range(len(text)):
        t = text[i].lower()
        t_place = alphabet.find(t)
        k = key[i].lower()
        k_place = alphabet.find(k)
        shift = k_place
        if t not in alphabet:
            decryption += text[i]
        else:
            if t_place - shift < 0:
                new_value = t_place - shift + len(alphabet)
            else:
                new_value = t_place - shift
            decryption += chr(new_value + 97)
    #print(text)
    #print(key)
    print(decryption)

def get_file_name(i):
    if i < 10:
        file_name = "file_00000" + str(i) + ".txt"
    elif i < 100:
        file_name = "file_0000" + str(i) + ".txt"
    elif i < 1000:
        file_name = "file_000" + str(i) + ".txt"
    elif i < 10000:
        file_name = "file_00" + str(i) + ".txt"
    else:
        file_name = "file_0" + str(i) + ".txt"
    return file_name

def find_vinegar():
    for i in range(18000):
        file_name = get_file_name(i)
        
        with open('text_files/' + file_name, 'r') as f:
            text = f.read()
            decryption = vinegar_decrypt(text, 'enigma')
            if 'essage' in decryption:
                print(file_name)
                print(decryption)

find_vinegar()
#vinegar_encrypt('Hello my name is casey', 'enigma')
