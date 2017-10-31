import json
import sys
from math import sqrt


def load_data(filepath):
    with open(filepath, encoding="utf8") as json_file_utf8:
        json_file_cont = json.loads(json_file_utf8.read())
    return json_file_cont


def get_biggest_bar(f_cont):
    return max(range(len(f_cont["features"])), key = lambda x: f_cont["features"][x]["properties"]["Attributes"]["SeatsCount"])


def get_smallest_bar(f_cont):
    return min(range(len(f_cont["features"])), key = lambda x: f_cont["features"][x]["properties"]["Attributes"]["SeatsCount"])


def get_closest_bar(f_cont, latt, longt):
    return min(range(len(f_cont["features"])),key = lambda x: sqrt((float(f_cont["features"][x]["geometry"]["coordinates"][0])-longt)**2+(float(f_cont["features"][x]["geometry"]["coordinates"][1])-latt)**2))


def print_barinfo(f_cont,item_num):
    print("Название: " + str(f_cont["features"][item_num]["properties"]["Attributes"]["Name"]))
    print("Телефон: " + str(f_cont["features"][item_num]["properties"]["Attributes"]["PublicPhone"][0]).replace("{'PublicPhone': '","").replace("'}",""))
    print("Адрес: " + str(f_cont["features"][item_num]["properties"]["Attributes"]["Address"]))
    print("Количество мест: " + str(f_cont["features"][item_num]["properties"]["Attributes"]["SeatsCount"]))
    print("Округ: " + str(f_cont["features"][item_num]["properties"]["Attributes"]["AdmArea"]))
    print("Район: " + str(f_cont["features"][item_num]["properties"]["Attributes"]["District"]))


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