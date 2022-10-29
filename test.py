import csv
import xml.etree.ElementTree as ET


tree = ET.parse('test_task.xml')
first_tag = tree.getroot()
user_list = first_tag.find('user')
users = user_list.find('users')
user = users.findall('user')

count = 0
list_xml = []
for obj in user:
    first_name = obj[0]
    last_name = obj[1]
    avatar = obj[2]
    if last_name.text is None or '(' in last_name.text:
        pass
    else:
        count += 1
        # if first_name.text == None or last_name.text == None or avatar.text == None:
        # print(f'{count}. {last_name.text}')
        list_xml.append([first_name.text, last_name.text, avatar.text])

with open('test_task.csv') as f:
    count_csv = 0
    list_csv = []
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if i == 0:
            pass
        else:
            if row[0] == '' or row[1] == '' or row[2] == '' or '(' in row[0]:
                pass
            else:
                count_csv += 1
                list_csv.append([row[0], row[1], row[2]])
                # print(f'{count_csv}. {row[0]}')

    # for lc in list_csv:
    #     print(lc)
    #
    # for lx in list_xml:
    #     print(lx[1])

    i = -1
    user_list = []
    for lx in list_xml:
        i += 1
        for lc in list_csv:
            if lx[1] in lc[0]:
                y = list_csv.index(lc)
                user_list.append(list_xml[i] + list_csv[y])
            else:
                pass

    for u in user_list:
        print(u)
