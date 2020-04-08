from AES import *


def read_data_from_binary_file(file_name: str):
    with open(file_name, 'rb') as bin_in:
        open_text = bin_in.read()

    return open_text


def read_key_and_iv(file_name: str):
    with open(file_name, 'rb') as bin_in:
        key = bin_in.readline(16)
        bin_in.readline()
        sync_package = bin_in.readline(16)

    return key, sync_package


def execute(aes: AES, operat: str, msg, iv):
    if operat == 'encrypt':
        with open('encrypt.bin', 'wb') as bin_out:
            cipher_text = aes.encrypt_cfb(msg, iv)

            bin_out.write(cipher_text)

    elif operat == 'decrypt':
        with open('decrypt.bin', 'wb') as bin_out:
            open_text = aes.decrypt_cfb(msg, iv)

            bin_out.write(open_text)


if __name__ == '__main__':
    file_name = input('Enter file name with data: ')

    data = read_data_from_binary_file(file_name)
    key, iv = read_key_and_iv('key.bin')

    aes = AES(key)

    operation = input('What do you want operation to execute?: ')

    execute(aes, operation, data, iv)
