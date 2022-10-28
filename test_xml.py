import xml.etree.ElementTree as ET


tree = ET.parse('test_task.xml')
first_tag = tree.getroot()
user_list = first_tag.find('user')
users = user_list.find('users')
user = users.findall('user')

count = 0
for obj in user:
    first_name = obj[0]
    last_name = obj[1]
    avatar = obj[2]
    count += 1
    # if first_name.text == None or last_name.text == None or avatar.text == None:
    print(f'{count}. {first_name.text} {last_name.text}, {avatar.text}')



