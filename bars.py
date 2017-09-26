import json
import sys
from math import sqrt

def load_data(filepath):
    with open(filepath, encoding="utf8") as json_file_utf8:
        json_file_utf8_content = json.loads(json_file_utf8.read())
    return json_file_utf8_content


def get_biggest_bar(json_file_utf8_content):
    #создание списка критериев (здесь - кол-во сидячих мест)
    criteria_list = []
    criteria_number = 0
    for item_self in json_file_utf8_content["features"]:
        criteria_list.append(json_file_utf8_content["features"][criteria_number]["properties"]["Attributes"]["SeatsCount"])
        criteria_number = criteria_number + 1
    #поиск номера нужного элемента в списке критериев
    for criteria_number, criteria in enumerate(criteria_list):
            if max(criteria_list) == criteria:
                criteria_number_result=criteria_number
    return json_file_utf8_content["features"][criteria_number_result]


def get_smallest_bar(json_file_utf8_content):
    #создание списка критериев (здесь - кол-во сидячих мест)
    criteria_list = []
    criteria_number = 0
    for item_self in json_file_utf8_content["features"]:
        criteria_list.append(json_file_utf8_content["features"][criteria_number]["properties"]["Attributes"]["SeatsCount"])
        criteria_number = criteria_number + 1
    #поиск номера нужного элемента в списке критериев
    for criteria_number, criteria in enumerate(criteria_list):
            if min(criteria_list) == criteria:
                criteria_number_result=criteria_number
    return json_file_utf8_content["features"][criteria_number_result]


def get_closest_bar(json_file_utf8_content, latitude, longitude):
    #создание списка критериев (здесь - кол-во сидячих мест)
    criteria_list = []
    criteria_number = 0
    for item_self in json_file_utf8_content["features"]:
        distance=sqrt((float(json_file_utf8_content["features"][criteria_number]["geometry"]["coordinates"][0])-longtitude)**2+(float(json_file_utf8_content["features"][criteria_number]["geometry"]["coordinates"][1])-latitude)**2)
        criteria_list.append(distance)
        criteria_number = criteria_number + 1
    #поиск номера нужного элемента в списке критериев
    for criteria_number, criteria in enumerate(criteria_list):
            if min(criteria_list) == criteria:
                criteria_number_result=criteria_number
    return json_file_utf8_content["features"][criteria_number_result]


def pretty_print_json(json_file_utf8_content):
    print(json.dumps(json_file_utf8_content, indent=4, ensure_ascii=False, sort_keys=True))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = (sys.argv[1].replace("'", "")).replace("\|", "/")
    else:
        filepath = 'bars.json'
    print("Самый крупный по количеству мест бар в Москве:")
    pretty_print_json(get_biggest_bar(load_data(filepath)))
    print()
    print("Самый маленький по количеству мест бар в Москве:")
    pretty_print_json(get_smallest_bar(load_data(filepath)))
    print()
    try:
        print("Для того чтобы определить ближайший к Вам бар, введите Ваши координаты")
        latitude = float(input("Широта: "))
        longtitude = float(input("Долгота: "))
        pretty_print_json(get_closest_bar(load_data(filepath), latitude, longtitude))
    except ValueError:
        print('введены данные не числового типа')
