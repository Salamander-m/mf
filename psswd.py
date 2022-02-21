import secrets
import string


def generate_alphanum_crypt_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    crypt_rand_string = ''.join(secrets.choice(
        letters_and_digits) for i in range(length))
    print("Cryptic Random string of length", length, "is:", crypt_rand_string)


generate_alphanum_crypt_string(16)