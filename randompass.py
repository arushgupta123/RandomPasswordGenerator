import secrets
import string

pwdL = int(input("How many integers do you want in your password?\n"))

letters = string.ascii_letters
digits = string.digits
specials = string.punctuation
#print(type(specials))

x = letters + digits + specials

pwd = ''

for i in range(pwdL):
    pwd += ''.join(secrets.choice(x))

print(pwd)
