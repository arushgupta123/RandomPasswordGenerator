import randompass_p
import datetime
import secrets
import string
time = datetime.datetime.now()



if time.hour < 12:
    print("Good morning! This is randoom password generator!")
elif 12 <= time.hour < 18:
    print("Good afternoon! THis is random password generator!")
elif time.hour > 18 or time.hour == 18:
    print("Good evening! This is random password generator")
else:
    print("This is random password generator")


choose = input("Chose between easy to remember password (type RP) and tough password(type TP)(You can try both also!):\n")

if choose == "RP" or choose == "rp" or choose == "Rp" or choose == "rP":
    print("Your new password is:")
    print(randompass_p.practicalPass["generatePPass"])
elif choose == "TP" or choose == "tp" or choose == "Tp" or choose == "tP":
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

else:
    print("Please type RP or TP. If you have typed it but still getting this message, then check whether you are putting spacebar before after or between the letters.")