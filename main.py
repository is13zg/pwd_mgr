from transliterate import translit
from init_data import db

db.create_new_pswd_table(str(translit("23424_своя2", reversed=True)))
db.add_pswd_record(str(translit("23424_своя2", reversed=True)), "1", "1", "1", "1", "1", "1", "1")
db.add_pswd_view(str(translit("23424_своя2", reversed=True)), "1", "22")
db.add_pswd_view(str(translit("23424_своя2", reversed=True)), "1", "33")
text = "личная"
print(translit(text, reversed=True))
print(translit("lichnaja", 'ru'))
