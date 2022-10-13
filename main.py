from transliterate import translit
from init_data import db

db.create_new_pswd_table(str(translit("23424_своя2", reversed=True)))

text = "личная"
print(translit(text, reversed=True))
print(translit("lichnaja",'ru'))
