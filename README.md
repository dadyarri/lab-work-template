# Шаблон лабораторной работы

Генерирует базовую структуру лабораторной работы на Python, устанавливает зависимости и генерирует шаблон отчёта

## Требования

- cookiecutter

- docxtpl

- poetry

`pip install cookiecutter docxtpl poetry`

## Настройка

`cookiecutter gh:dadyarri/lab-work-template`

## Синтакис шаблона

Цель работы и вывода:
    Находятся в начале сгенерированного файла, заключены между тегами Goal/EndGoal для цели и Summary/EndSummary для вывода

## Скрипты

### Требования

#### Linux

`sudo apt install make` - Debian  
`sudo pacman -S base-devel` - Arch

#### Windows

Для работы со скриптами make на Windows, нужно [установить](https://chocolatey.org/install) chocolatey

`choco install make`


### Генерация отчёта

Подстановка в Word-файл переменных, заданных на этапе создания шаблона, сбор цели работы, вывода из исходного кода и вставка в отчёт

`make insert`


### Тестирование кода

Запуск юнит-тестов написанных с помощью pytest

`make tests`