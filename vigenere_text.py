import string

text = "Nitesh Choudhary"
key = "vigenerealgorithm"

def vigenere(text, key, direction=1):
    alphabets = string.ascii_lowercase
    encrypted_text = ""
    key_index = 0

    for char in text.lower():
        if not char.isalpha():
            encrypted_text += char
        else:
            key_character = key[key_index % len(key)]
            key_index += 1
            offset = alphabets.index(key_character)
            index = (alphabets.find(char) + offset * direction) % len(alphabets)
            encrypted_text += alphabets[index]
    return encrypted_text


encrypted_text = vigenere(text, key)
decrypted_text = vigenere(encrypted_text, key, -1)

print(encrypted_text)
print(decrypted_text)
