import json


class Residents:

    def __init__(self, id, name, fname, county, age, is_teen):
        self.id = id
        self.name = name
        self.fname = fname
        self.county = county
        self.age = age
        self.is_teen = is_teen

    def __repr__(self):
        return 'номер: %s, имя: %s, пол: %s, страна: %s, возраст: %s, совершеннолетие: %s' % \
               (self.id, self.name, self.fname, self.county, self.age, self.is_teen)

    def same_age(self, age):
        return self.age == age

    def older_age(self, age):
        return self.age > age

    def younger_age(self, age):
        return self.age <= age

    def underage(self):
        return (self.age >= 18 and self.county == 'Russia') or \
               (self.age >= 20 and self.county == 'Japan') or \
               (self.age >= 21 and self.county == 'USA') or \
               (self.age >= 20 and self.county == 'Thailand')

    def bad_users(self):
        return self.underage() == self.is_teen


def user(basa):
    for human in basa:
        Human = Residents(human.get('id'), human.get('name'), human.get('fname'), human.get('county'), human.get('age'), human.get('is_teen'))
        return Human


with open('users_ds.json', 'r') as basa:
    users_basa = json.load(basa)

print('Введите нужную Страну')
if user(users_basa).county == input():
    print('jhkh')

print('Введите возраст, чтобы найти всех с таким возрастом')
age_split = int(input())
for user in users_basa:
    human = Residents(user.get('id'), user.get('name'), user.get('fname'), user.get('county'), user.get('age'),
                      user.get('is_teen'))
    if human.same_age(age_split):
        print(user)

print('Введите возрат, чтобы найти всех старше этого возраста')
age_old_split = int(input())
for user in users_basa:
    human = Residents(user.get('id'), user.get('name'), user.get('fname'), user.get('county'), user.get('age'),
                      user.get('is_teen'))
    if human.older_age(age_old_split):
        print(user)

print('Введите возраст, чтобы найти всех младше или равного этого возраста')
age_young_split = int(input())
for user in users_basa:
    human = Residents(user.get('id'), user.get('name'), user.get('fname'), user.get('county'), user.get('age'),
                      user.get('is_teen'))
    if human.younger_age(age_young_split):
        print(user)

print('Все совершеннолетние')
for user in users_basa:
    human = Residents(user.get('id'), user.get('name'), user.get('fname'), user.get('county'), user.get('age'),
                      user.get('is_teen'))
    if human.underage():
        print(user)

print('Все несовершеннолетние')
for user in users_basa:
    human = Residents(user.get('id'), user.get('name'), user.get('fname'), user.get('county'), user.get('age'),
                      user.get('is_teen'))
    if not human.underage():
        print(user)

print('битые записи')
for user in users_basa:
    human = Residents(user.get('id'), user.get('name'), user.get('fname'), user.get('county'), user.get('age'),
                      user.get('is_teen'))
    if human.bad_users():
        print(user)



