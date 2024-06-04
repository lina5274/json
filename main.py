#
# Небольшой компании срочно нужен тот, кто может умело обращаться с JSON фалами, т.к. вся их база данных,
# к сожалению, основана на хранении именно в таком формате.
# Менять всё и организовывать реляционную базу данных слишком долго и дорого, да и данных многовато,
# нужно быстрое и дешёвое решение, хоть и не самое правильное... Ну а что поделать, задача есть, нужно решать.
#
# Напишите функцию employees_rewrite(sort_type), которая:
# Принимает параметром тип сортировки (ключ) - sort_type.
# Функция должна:
# Получить данные из employees.json и записать в employees_[sort_type]_sorted.json:
# Формат записи должен быть как в исходном файле.
# Если сортировка производится по строковым значения, то в алфавитном порядке.
# Если сортировка производится по числовым значениям, то в порядке убывания.


import json

# def employees_rewrite(sort_type):
#
#     with open('employees.json','r') as read_file:
#         data = json.load(read_file)
#
#         data['employees'].sort(key=lambda x: x[sort_type], reverse=isinstance(data['employees'][0][sort_type], int)
#
#         sorted_data = json.dumps(data, sort_keys=True)
#
#     with open('employees_lastname_sorted.json', 'w') as write_file:
#         json.dump(sorted_data, write_file)

def employees_rewrite(sort_type):
    with open('employees.json', 'r') as f:
        data = json.load(f)

    if sort_type not in data['employees'][0]:
        raise ValueError('Bad key for sorting')

    data['employees'].sort(key=lambda x: x[sort_type], reverse=isinstance(data['employees'][0][sort_type], int))

    with open(f'employees_{sort_type}_sorted.json',
              'w') as f:
        json.dump(data, f, ensure_ascii=False)

    print(
        f"Сотрудники успешно отсортированы по ключу '{sort_type}' и записаны в файл 'employees_{sort_type}_sorted.json'")


employees_rewrite('lastName')
employees_rewrite('department')
employees_rewrite('salary')
employees_rewrite('firstName')




