# Бары

Проект предназачен для определения самого большого и самого маленького бара (критерий - количество мест),а также
определения ближайшего бара (критерий - расстояние по прямой до бара от точки, координаты которой вводятся вручную)

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Windows:

```#!bash

$ python bars.py bars.json
```


Пример вывода данных
```
Самый крупный по количеству мест бар в Москве:
Название: Спорт бар «Красная машина»
Телефон: (905) 795-15-84
Адрес: Автозаводская улица, дом 23, строение 1
Количество мест: 450
Округ: Южный административный округ
Район: Даниловский район
 
Самый маленький по количеству мест бар в Москве:
Название: БАР. СОКИ
Телефон: (495) 258-94-19
Адрес: Дубравная улица, дом 34/29
Количество мест: 0
Округ: Северо-Западный административный округ
Район: район Митино
 
Для того чтобы определить ближайший к Вам бар, введите Ваши координаты
 
Широта: 55
Долгота: 35
 
Ближайший бар:
Название: Staropramen
Телефон: (985) 069-34-47
Адрес: Садовая-Спасская улица, дом 19, корпус 1
Количество мест: 50
Округ: Центральный административный округ
Район: Красносельский район
```

Запуск на Linux происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
