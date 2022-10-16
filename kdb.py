from pykeepass import PyKeePass, create_database
import os.path


def create_new_kdb(kdb_name, key):
    if not os.path.isfile(kdb_name + '.kdbx'):
        kp = create_database(kdb_name + '.kdbx', password=key, keyfile=None, transformed_key=None)
        kp.add_group(kp.root_group, 'general')
        kp.save()


def add_kdb_group(kdb_name, key, group_name):
    kp = PyKeePass(kdb_name + '.kdbx', password=key)
    found_group = kp.find_groups(name=group_name)
    if found_group == []:
        kp.add_group(kp.root_group, group_name)
        kp.save()
    else:
        print(f"Group by name [{group_name}] already exist. Group NOT add.")


def add_kdb_record(kdb_name, key, group="general", title="record_name", username="login", password="pswd", url=None,
                   notes=None):
    kp = PyKeePass(kdb_name + '.kdbx', password=key)
    found_group = kp.find_groups(name=group, first=True)
    if found_group != None:
        kp.add_entry(found_group, title=title, username=username, password=password, url=url,
                     notes=notes)
        kp.save()
    else:
        print(f"Group by name [{group}] not found. Entry NOT add.")


def get_kdb_groups(kdb_name, key):
    kp = PyKeePass(kdb_name + '.kdbx', password=key)
    return list(map(lambda x: str(x)[8:-1], kp.groups))[1:]


def find_entries(kdb_name, key, search):
    kp = PyKeePass(kdb_name + '.kdbx', password=key)
    res = list()
    res.extend(list(kp.find_entries(title=search + '.*', regex=True)))
    t_res = list(kp.find_entries(username=search + '.*', regex=True))
    for entry in t_res:
        if entry not in res:
            res.append(entry)
    t_res = list(kp.find_entries(url=search + '.*', regex=True))
    for entry in t_res:
        if entry not in res:
            res.append(entry)
    t_res = list(kp.find_entries(notes=search + '.*', regex=True))
    for entry in t_res:
        if entry not in res:
            res.append(entry)
    print(res)


def del_kdb_record():
    pass


# load database
create_new_kdb('newDb', 's3cr3t')
find_entries('newDb', 's3cr3t', "1")
