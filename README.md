﻿
Создать django проект который управляет базой студентов,
Сущности:
 - Студент - ФИО, дата-рождения, №студ-билета, группа(FK(Группа))
 - Группа - Название, староста(FK(Студент))
 
Проект должен быть сконфигурирован на sqlite и иметь фикстуру
initial_data.json с подготовленными данными(несколько групп и студентов)

Создать следующие views:
         - список групп (таблица - название, кол-во человек в группе, староста)
	 - при нажатии на группу - страница с со списком студентов для этой группы
	 - создание/редактирование/удаление  групп/студентов Добавить авторизацию для этих страниц (username/password)

Сделать middleware который на всех страницах(content-type ==
text/html) добавляет время выполнения запроса и количество sql
запросов(перед закрывающим тегом </body>)

Django.Admin - создать admin views для Групп/студентов (студенты
так же должны быть как inline для Групп)

Шаблоны/Контекст - сделать template-context-processor который
добавляет django.settings в контекст шаблонов

Шаблоны/Теги - написать тег который принимает любой объект и
рендерит ссылку на его редактирование в админке (например {% edit_list
request.user %})

Django.TestFramework - написать django-testcase (unittest) который
логинится на сайт, добавляет группу и студента в созданную группу

