def switcharoo(text):
    result = ""
    for c in text:
        n = ord(c)
        new_value = 158 - n
        new_letter = chr(new_value)
        result += new_letter
    return result

with open("text_files/file_010882.txt", 'r') as f:
    text = f.read()

print(switcharoo(text))
