import secrets
"""
adjective = ("Thirsty","hungry","gigantic", "Chocolate", "Fizzy", "blushing", "SmArT")
object = ("cow", "man", "dogs","camel", "pigs", "cats", "hurricane", "mexican", "SpORTSmen")
additive = ("1z&", "3f@g","6g!ht","7yh$d", "4rd#")

passw = adjective + object + additive
#for i in range(3):
   #pas = ''.join(secrets.choice(passw))
print(secrets.choice(adjective) + secrets.choice(object) + secrets.choice(additive))
"""
practicalPass = {
    "adjective": ("Thirsty","hungry","gigantic", "Chocolate", "Fizzy", "blushing", "SmArT"),
    "object": ("cow", "man", "dogs","camel", "pigs", "cats", "hurricane", "mexican", "SpORTSmen"),
    "additive": ("1z&", "3f@g","6g!ht","7yh$d", "4rd#"),
    "generatePPass": ''.join(secrets.choice(("Thirsty","hungry","gigantic", "Chocolate", "Fizzy", "blushing", "SmArT")) + secrets.choice(("cow", "man", "dogs","camel", "pigs", "cats", "hurricane", "mexican", "SpORTSmen")) + secrets.choice(("1z&", "3f@g","6g!ht","7yh$d", "4rd#")))
}

#print(practicalPass["generatePPass"])