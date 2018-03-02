import random

def generate_random_text(num_chars):
    text = ""

    for i in range(num_chars):
        r = random.randint(32, 126)
        text += chr(r)
    
    return text


def mean(counts):
    total = 0
    
    for n in counts:
        total += n
    average = total / len(counts)
    return average
    

def chi_square(counts):
    expected = mean(counts)
    
    x = 0

    for n in counts:
        observed = n
        x += (observed - expected)**2
        
    return x / expected

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

def message_finder():
    for i in range(18000):
        file_name = get_file_name(i)
            
        with open("text_files/" + file_name, 'r') as f:
            content = f.read()
            counts = [0] * 127

            for c in content:
                n = ord(c)
                counts[n] += 1
    
            counts = counts[32:127]
            x_square = chi_square(counts)
            if x_square > 150:
                print(file_name)
                print(x_square)
            elif 'ensaje' in content:
                print("Spanish: " + file_name)
                print(x_square)
            
def make_random_files():
    for i in range(20):
        content = generate_random_text(18000)
        with open("random_text_files/random_text_file" + str(i), 'w') as f:
            f.write(content)
    for i in range(20):
        with open("random_text_files/random_text_file" + str(i), 'r') as f:
            content = f.read()
            counts = [0] * 127

            for c in content:
                n = ord(c)
                counts[n] += 1
        
            counts = counts[32:127]
            print(chi_square(counts))


message_finder()





# code here to write content to a file
