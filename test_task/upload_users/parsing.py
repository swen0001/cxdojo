import xml.etree.ElementTree as ET
import csv


def parsing_xml(file_xml_path: str) -> list:
    tree = ET.parse(file_xml_path)
    first_tag = tree.getroot()
    user_list = first_tag.find('user')
    users = user_list.find('users')
    user = users.findall('user')

    list_xml = []
    for obj in user:
        first_name = obj[0]
        last_name = obj[1]
        avatar = obj[2]
        if last_name.text is None or '(' in last_name.text:
            pass
        else:
            list_xml.append([first_name.text, last_name.text, avatar.text])
    return list_xml


def parsing_csv(file_csv_path: str) -> list:
    with open(file_csv_path, 'r') as f:
        list_csv = []
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                pass
            else:
                if row[0] == '' or row[1] == '' or row[2] == '' or '(' in row[0]:
                    pass
                else:
                    list_csv.append([row[0], row[1], row[2]])
    return list_csv
