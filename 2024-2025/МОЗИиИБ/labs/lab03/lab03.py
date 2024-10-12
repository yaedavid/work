russian_letters = [chr(i) for i in range(ord('А'), ord('Я') + 1)]

def xor_cipher(text, password):   
    data = []
    for char in text:
        data.append(russian_letters.index(char))
    key = []
    repeated_password = (password * (len(text) // len(password) + 1))[:len(text)]
    for char in repeated_password:
        key.append(russian_letters.index(char))
    cryptogram = []
    for i in range(len(text)):
        index = (data[i]+key[i]+1) % len(russian_letters)
        cryptogram.append(russian_letters[index])
    result = ''.join(cryptogram)
    return result

text = input('Введите текст: ').upper()
filter_text = ''.join(char for char in text if char in russian_letters)
password = input('Введите пароль: ').upper()
filter_password = ''.join(char for char in password if char in russian_letters)
if len(filter_text) >= len(filter_password):
    encrypted_xor = xor_cipher(filter_text, filter_password)
    print("Криптограмма:", encrypted_xor)