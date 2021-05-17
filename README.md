# Шаблон лабораторной работы

Генерирует базовую структуру лабораторной работы на Python, устанавливает зависимости и генерирует шаблон отчёта

## Требования

- cookiecutter

- docxtpl

- poetry

- git

- make

`pip install git+https://github.com/cookiecutter/cookiecutter docxtpl poetry`

### Linux

`sudo apt install make` - Debian  
`sudo pacman -S --needed base-devel git` - Arch

### Windows

Необходима утилита для установки сторонних пакетов: [chocolatey](https://chocolatey.org/install)

`choco install make git python`

## Настройка

`cookiecutter gh:dadyarri/lab-work-template`

## Синтаксис шаблона

Цель работы и вывод:
    Находятся в файле metainfo.txt, заключены между тегами Goal/EndGoal для цели и Summary/EndSummary для вывода (пример в генерируемом скрипте)

## Скрипты

### Генерация отчёта

Подстановка в Word-файл переменных, заданных на этапе создания шаблона, сбор цели работы, вывода из исходного кода и вставка в отчёт

`make insert`


### Тестирование кода

Запуск юнит-тестов написанных с помощью pytest

`make tests`
