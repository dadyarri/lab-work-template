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

## Генерация отчёта

### Linux

`make insert`


### Windows

Для работы со скриптами make на Windows, нужно [установить](https://chocolatey.org/install) chocolatey

`choco install make`

`make insert`
