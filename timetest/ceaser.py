def caesar_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 3
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

input_string = input()
encrypted_string = caesar_cipher(input_string)
print(encrypted_string)