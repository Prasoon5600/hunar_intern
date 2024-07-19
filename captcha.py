import random
import string

def generate_captcha():
    captcha_characters = string.ascii_letters + string.digits  # Contains a-z, A-Z, 0-9
    captcha = ''.join(random.choice(captcha_characters) for _ in range(5))
    return captcha

captcha = generate_captcha()
print(captcha)
