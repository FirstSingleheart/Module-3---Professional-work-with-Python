from pprint import pprint
import csv
import re

# phone_pattern = r"(\+7|8)?\s*\((\d+)\)\s*(\d+)[-\s](\d+)[-\s](\d+)\s*(\(*)(\w*\.)*\s*(\d{4})*(\))*"
# phone_sub = r"+7(\3)\6-\8-\10 \12\13"

phone_pattern = '(8|\+7)?\s*(\(*)(\d{3})(\)*)(\s*|-)(\d{3})(\s*|-)(\d{2})(\s*|-)(\d{2})\s*(\(*)(\w\w\w\.)*\s*(\d{4})*(\))*'
phone_sub = r'+7(\3)\6-\8-\10 \12\13'

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)


def change_contact_list(list_name):
    new_contacts_list = []
    for contact in list_name:
        new_contact = []
        full_name = ", ".join(contact[:3])
        result = re.findall(r'(\w+)', full_name)
        while len(result) < 3:
            result.append('')
        new_contact += result
        new_contact.append(contact[3])
        new_contact.append(contact[4])
        phone = re.compile(phone_pattern)
        new_phone = phone.sub(phone_sub, contact[5])
        new_contact.append(new_phone)
        new_contact.append(contact[6])
        new_contacts_list.append(new_contact)
    return new_contacts_list


def delete_duplicates(list_name):
    phone_book = {}
    for contact in list_name:
        if contact[0] in phone_book:
            contact_value = phone_book[contact[0]]
            for i in range(len(contact_value)):
                if contact[i]:
                    contact_value[i] = contact[i]
        else:
            phone_book[contact[0]] = contact
    final_list = phone_book.values()
    return list(final_list)


c_c_l = change_contact_list(contacts_list)
d_d = delete_duplicates(c_c_l)

with open("phonebook.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerows(d_d)

