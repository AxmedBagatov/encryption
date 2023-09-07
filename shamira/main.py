def generate_keys():
    """Генерация открытого и закрытого ключей"""
    p = 61  # Простое число p
    q = 53  # Простое число q
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 17  # Открытый ключ e
    d = multiplicative_inverse(e, phi)  # Закрытый ключ d

    return (e, n), (d, n)

def multiplicative_inverse(a, b):
    """Нахождение мультипликативного обратного"""
    if b == 0:
        return 1
    x1, x2, y1, y2 = 0, 1, 1, 0
    while b > 0:
        q, r = divmod(a, b)
        x = x2 - q * x1
        y = y2 - q * y1
        a, b, x2, x1, y2, y1 = b, r, x1, x, y1, y
    return x2

def encrypt(message, public_key):
    """Шифрование сообщения"""
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def decrypt(encrypted_message, private_key):
    """Дешифрование сообщения"""
    d, n = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return ''.join(decrypted_message)

# Генерация открытого и закрытого ключей
public_key, private_key = generate_keys()

# Ввод сообщения для шифрования
message = input("Введите сообщение для шифрования: ")

# Шифрование сообщения
encrypted_message = encrypt(message, public_key)
print("Зашифрованное сообщение:", encrypted_message)

# Дешифрование сообщения
decrypted_message = decrypt(encrypted_message, private_key)
print("Дешифрованное сообщение:", decrypted_message)
