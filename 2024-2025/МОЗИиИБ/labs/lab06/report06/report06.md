---
# Front matter
lang: ru-RU
title: "Лабораторная работа №6"
subtitle: "Дисциплина: Математические основы защиты информации и информационной безопасности"
author: "Аветисян Давид Артурович"

# Formatting
toc-title: "Содержание"
toc: true # Table of contents
toc_depth: 2
lof: true # Список рисунков
lot: true # Список таблиц
fontsize: 12pt
linestretch: 1.5
papersize: a4paper
documentclass: scrreprt
polyglossia-lang: russian
polyglossia-otherlangs: english
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase
indent: true
pdf-engine: lualatex
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Реализовать алгоритм, реализующий p-метод Полларда.

# Задание

1. Реализовать алгоритм, реализующий p-метод Полларда.
2. Разложить на множители данное преподавателем число.

# Выполнение лабораторной работы

Данная работа была выполнена на языке Julia.

Для реализации алгоритм, реализующего p-метод Полларда, была написана следующая программа.

![Алгоритм, реализующий p-метод Полларда, на языке Julia](image06/image_01.png){ width=70% }

В данной программе:  
- 1-й блок. Импорт необходимых модулей  
- 2-й блок. Реализация самого алгоритма: Задаются начальные значения $x$ и $y$ и НОД $d$. С помощью цикла вычисляется медленный и быстрый шаги $x$ и $y$. Затем они сравниваются, чтобы найти НОД. В конце проверяется результат выполнения алгоритма.  
- 3-й блок. Задаётся значение $n$, для которого нужно найти делитель и вызывается функция, описанная выше.  
- 4-й блок. Вывод ответа в зависмости от результат выполнения алгоритма.

Мы можем видеть результат для чисел 8051 и 1359331 (данное преподавателем число) на рисунке выше. Программа работает верно.

# Выводы

Я реализовал алгоритм, реализующий p-метод Полларда.
