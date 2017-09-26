# Бары

Проект предназачен для определения самого большого и самого маленького бара (критерий - количество мест),а также
определения ближайшего бара (критерий - расстояние по прямой до бара от точки, координаты которой вводятся вручную)
В качестве данных по умолчанию используется список баров в формате .json с сайта data.mos.ru 

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Windows:

```#!bash

$ python bars.py #в качестве опционального параметра может быть использован путь к файлу .json c информацией о барах с сайта data.mos.ru
```


Пример вывода данных
```
Самый крупный по количеству мест бар в Москве:
{
    "geometry": {
        "coordinates": [
            37.638228501070095,
            55.70111462948684
        ],
        "type": "Point"
    },
    "properties": {
        "Attributes": {
            "Address": "Автозаводская улица, дом 23, строение 1",
            "AdmArea": "Южный административный округ",
            "District": "Даниловский район",
            "IsNetObject": "нет",
            "Name": "Спорт бар «Красная машина»",
            "OperatingCompany": null,
            "PublicPhone": [
                {
                    "PublicPhone": "(905) 795-15-84"
                }
            ],
            "SeatsCount": 450,
            "SocialPrivileges": "нет",
            "global_id": 169375059
        },
        "DatasetId": 1796,
        "ReleaseNumber": 2,
        "RowId": "fbe6c340-4707-4d74-b7ca-2b84a23bf3a8",
        "VersionNumber": 2
    },
    "type": "Feature"
}

Самый маленький по количеству мест бар в Москве:
{
    "geometry": {
        "coordinates": [
            37.649759000274265,
            55.871183000126486
        ],
        "type": "Point"
    },
    "properties": {
        "Attributes": {
            "Address": "проезд Дежнёва, дом 1",
            "AdmArea": "Северо-Восточный административный округ",
            "District": "район Южное Медведково",
            "IsNetObject": "нет",
            "Name": "Бар в Деловом центре Яуза",
            "OperatingCompany": null,
            "PublicPhone": [
                {
                    "PublicPhone": "нет телефона"
                }
            ],
            "SeatsCount": 0,
            "SocialPrivileges": "нет",
            "global_id": 272459485
        },
        "DatasetId": 1796,
        "ReleaseNumber": 2,
        "RowId": "a3156c38-2b15-4088-98c7-d9ce24075827",
        "VersionNumber": 2
    },
    "type": "Feature"
}

Для того чтобы определить ближайший к Вам бар, введите Ваши координаты
Широта: 57
Долгота: 38
{
    "geometry": {
        "coordinates": [
            37.744234974114,
            55.917568731248
        ],
        "type": "Point"
    },
    "properties": {
        "Attributes": {
            "Address": "город Зеленоград, корпус 315",
            "AdmArea": "Зеленоградский административный округ",
            "District": "район Савёлки",
            "IsNetObject": "нет",
            "Name": "Гудсон бар",
            "OperatingCompany": null,
            "PublicPhone": [
                {
                    "PublicPhone": "(499) 740-97-58"
                }
            ],
            "SeatsCount": 30,
            "SocialPrivileges": "нет",
            "global_id": 281494735
        },
        "DatasetId": 1796,
        "ReleaseNumber": 2,
        "RowId": "243b42c4-294d-451e-919b-0d65b9811c84",
        "VersionNumber": 2
    },
    "type": "Feature"
}

```

Запуск на Linux происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
