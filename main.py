from transliterate import translit
from init_data import db

db.create_new_pswd_table(str(translit("23424_своя2", reversed=True)))
db.add_pswd_record(str(translit("23424_своя2", reversed=True)), 'name', 'login', 'E_pswd', 'url', 'E_secret', 'comment',
                   'E_who_view')
db.add_pswd_view(str(translit("23424_своя2", reversed=True)), "1", "22")
db.add_pswd_view(str(translit("23424_своя2", reversed=True)), "1", "33")
print(db.get_all_pswds(str(translit("23424_своя2", reversed=True))))
text = "личная"
print(translit(text, reversed=True))
print(translit("lichnaja", 'ru'))
