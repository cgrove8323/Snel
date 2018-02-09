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
    
'''def get_observed():
    '''
def chi_square(counts):
    expected = mean(counts)
    
    X = 0

    for n in counts:
        pass

    return X



'bunch_of_text = "asdfhjkjaewhfkljsadhflkjhasedfi9835u2xifu-q3ymtocfjd;sk^%$#^YJH&I*^%$*%TNIOUYTYU^RYI^RGLKHNJJKYTB"

counts = [0] * 127
print(counts)

generate_random_text(100)
for c in text:
    n = ord(c)
    counts[n] += 1

print(counts)
mean(counts)
print(mean(counts))


content = generate_random_text(100)

# code here to write content to a file
