import json
import sys
from math import sqrt

def load_data(filepath):
    with open(filepath, encoding="utf8") as json_file_utf8:
        json_file_utf8_content = json.loads(json_file_utf8.read())
    return json_file_utf8_content


def get_biggest_bar(json_file_utf8_content):

    criteria_list = []
    criteria_number = 0
    for item_self in json_file_utf8_content["features"]:
        criteria_list.append(json_file_utf8_content["features"][criteria_number]["properties"]["Attributes"]["SeatsCount"])
        criteria_number = criteria_number + 1
    return criteria_list.index(max(criteria_list))


def get_smallest_bar(json_file_utf8_content):

    criteria_list = []
    criteria_number = 0
    for item_self in json_file_utf8_content["features"]:
        criteria_list.append(json_file_utf8_content["features"][criteria_number]["properties"]["Attributes"]["SeatsCount"])
        criteria_number = criteria_number + 1
    return criteria_list.index(min(criteria_list))


def get_closest_bar(json_file_utf8_content, latitude, longitude):

    criteria_list = []
    criteria_number = 0
    for item_self in json_file_utf8_content["features"]:
        distance=sqrt((float(json_file_utf8_content["features"][criteria_number]["geometry"]["coordinates"][0])-longtitude)**2+(float(json_file_utf8_content["features"][criteria_number]["geometry"]["coordinates"][1])-latitude)**2)
        criteria_list.append(distance)
        criteria_number = criteria_number + 1
    return criteria_list.index(min(criteria_list))


def print_barinfo(json_file_utf8_content,criteria_number_result):

    print("Название: " + str(json_file_utf8_content["features"][criteria_number_result]["properties"]["Attributes"]["Name"]))
    print("Телефон: " + str(json_file_utf8_content["features"][criteria_number_result]["properties"]["Attributes"]["PublicPhone"][0]).replace("{'PublicPhone': '","").replace("'}",""))
    print("Адрес: " + str(json_file_utf8_content["features"][criteria_number_result]["properties"]["Attributes"]["Address"]))
    print("Количество мест: " + str(json_file_utf8_content["features"][criteria_number_result]["properties"]["Attributes"]["SeatsCount"]))
    print("Округ: " + str(json_file_utf8_content["features"][criteria_number_result]["properties"]["Attributes"]["AdmArea"]))
    print("Район: " + str(json_file_utf8_content["features"][criteria_number_result]["properties"]["Attributes"]["District"]))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = (sys.argv[1])
    else:
        print("Введите путь к файлу с информацией о барах")
        filepath = input()
    bars_info = load_data(filepath)
    print("Самый крупный по количеству мест бар в Москве:")
    print_barinfo(bars_info, get_biggest_bar(bars_info))
    print()
    print("Самый маленький по количеству мест бар в Москве:")
    print_barinfo(bars_info, get_smallest_bar(bars_info))
    print()
    try:
        print("Для того чтобы определить ближайший к Вам бар, введите Ваши координаты")
        latitude = float(input("Широта: "))
        longtitude = float(input("Долгота: "))
        print("Ближайший бар:")
        print_barinfo(bars_info, get_closest_bar(bars_info, latitude, longtitude))
    except ValueError:
        print('введены данные не числового типа')
