import random

def generate_keys():
    p = generate_prime_number()
    q = generate_prime_number()
    n = p * q
    phi = (p - 1) * (q - 1)

##    e = 17  # Открытый ключ e
    e = 65537
    d = multiplicative_inverse(e, phi)  # Закрытый ключ d

    return (e, n), (d, n)

def generate_prime_number():
    prime = False
    while not prime:
        num = random.randint(2, 100)  # Измените диапазон по своему усмотрению
        prime = is_prime(num)
    return num

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def multiplicative_inverse(a, b):
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
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return ''.join(decrypted_message)

while True:
    print("Меню:")
    print("1. Шифрование")
    print("2. Дешифрование")
    print("3. Выход")

    choice = input("Выберите режим (1, 2 или 3): ")

    if choice == '1':
        # Генерация открытого и закрытого ключей
        public_key, private_key = generate_keys()

        # Ввод сообщения для шифрования
        message = input("Введите сообщение для шифрования: ")

        # Шифрование сообщения
        encrypted_message = encrypt(message, public_key)
        print("Зашифрованное сообщение:", encrypted_message)
        print()

    elif choice == '2':
        # Ввод зашифрованного сообщения
        encrypted_message = input("Введите зашифрованное сообщение: ")

        # Дешифрование сообщения
        decrypted_message = decrypt(eval(encrypted_message), private_key)
        print("Дешифрованное сообщение:", decrypted_message)
        print()

    elif choice == '3':
        break

    else:
        print("Не правильный ввод.")
        print()
