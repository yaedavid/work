---
# Front matter
lang: ru-RU
title: "Лабораторная работа №5"
subtitle: "Дисциплина: Computer Skills for Scientific Writing"
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

Изучить создание и оформление таблиц в системе LaTeX. Освоить пакеты *array*, *booktabs*, *tabularx*, *longtable*, *threeparttable*, *siunitx* и приёмы, позволяющие делать таблицы профессионального вида.

# Задание

1. The array package.
2. Adding rules (lines).
3. Merging cells.
4. The other preamble contents.
5. Customizing booktabs rules.
6. Numeric alignment in columns.
7. Specifying the total table width.
8. Multi-page tables.
9. Table notes.
10. Typesetting in narrow columns.
11. Vertical tricks.
12. Line spacing in tables.

# Выполнение лабораторной работы

### The array package

В начале создаётся минимальная таблица из трёх колонок. Каждая ячейка отделяется знаком &, строка завершается \\\\.

![table.tex](image05/image_01_1.png){ width=70% }

![table.pdf](image05/image_01_2.png){ width=70% }

Для длинных колонок применяют тип колонки p{} с указанием ширины, что позволяет переносить текст внутри ячейки.

![new table.tex](image05/image_02_1.png){ width=70% }

![new table.pdf](image05/image_02_2.png){ width=70% }

### Adding rules (lines)

Для профессионального оформления использован пакет *booktabs*. Он заменяет *hline* на типографские аккуратные линии.

![table2.tex](image05/image_03_1.png){ width=70% }

![table2.pdf](image05/image_03_2.png){ width=70% }

Линии *toprule*, *midrule* и *bottomrule* формируют верхнюю, среднюю и нижнюю границы таблицы. Команда *cmidrule* даёт возможность проводить линии только под некоторыми колонками, что удобно при группировке данных. 

![new table2.tex](image05/image_04_1.png){ width=70% }

![new table2.pdf](image05/image_04_2.png){ width=70% }

Чтобы улучшить читаемость таблицы используется *addlinespace*, добавляющая небольшой промежуток между строками.

![new new table2.tex](image05/image_05_1.png){ width=70% }

![new new table2.pdf](image05/image_05_2.png){ width=70% }

### Merging cells

Команда *multicolumn* используется для объединения нескольких колонок в одной ячейке (например, для заголовков).

![table3.tex](image05/image_06_1.png){ width=70% }

![table3.pdf](image05/image_06_2.png){ width=70% }

Группировка данных в таблице. Первая колонка содержит названия групп. Пустые ячейки оставлены для визуального объединения строк внутри группы.

![new table3.tex](image05/image_07_1.png){ width=70% }

![new table3.pdf](image05/image_07_2.png){ width=70% }

### The other preamble contents

С помощью >{} и <{} можно добавлять оформление отдельным колонкам. 

![table4.tex](image05/image_08_1.png){ width=70% }

![table4.pdf](image05/image_08_2.png){ width=70% }

Межколоночные отступы и границы. Различные варианты показывают, как можно управлять расстоянием между колонками и вставлять дополнительные разделители внутри таблицы.

![new table4.tex](image05/image_09_1.png){ width=70% }

![new table4.pdf](image05/image_09_2.png){ width=70% }

### Customizing booktabs rules

Команды *toprule[2pt]*, *midrule[1pt]* и *cmidrule[0.5pt]* меняют толщину линий, что позволяет визуально разделять части таблицы. \

![table5.tex](image05/image_10_1.png){ width=70% }

![table5.pdf](image05/image_10_2.png){ width=70% }

### Numeric alignment in columns

Пакет *siunitx* автоматически выравнивает числа по десятичной точке, делая таблицу читабельной для сравнения значений.

![table6.tex](image05/image_11_1.png){ width=70% }

![table6.pdf](image05/image_11_2.png){ width=70% }

### Specifying the total table width

*tabular*\* растягивает таблицу на заданную долю ширины страницы, а *tabularx* автоматически подбирает ширину последней колонки для равномерного заполнения пространства.

![table7.tex](image05/image_12_1.png){ width=70% }

![table7.pdf](image05/image_12_2.png){ width=70% }

### Multi-page tables

Окружение *longtable* позволяет таблице автоматически переноситься на новую страницу, сохраняя заголовки. 

![table8.tex](image05/image_13_1.png){ width=70% }

![table8.pdf](image05/image_13_2.png){ width=70% }

### Table notes

Пакет *threeparttable* добавляет сноски к таблицам в виде пронумерованных заметок под основным содержимым.

![table9.tex](image05/image_14_1.png){ width=70% }

![table9.pdf](image05/image_14_2.png){ width=70% }

### Typesetting in narrow columns

Показано сравнение разных способов выравнивания текста в узких колонках (left, raggedright, RaggedRight)

![table10.tex](image05/image_15_1.png){ width=70% }

![table10.pdf](image05/image_15_2.png){ width=70% }

### Vertical tricks

Комбинированные таблицы в ячейках (@{}c@{}) используются для вертикального совмещения текста и подписей.

![table11.tex](image05/image_16_1.png){ width=70% }

![table11.pdf](image05/image_16_2.png){ width=70% }

### Line spacing in tables

Команда *setlength* изменяет высоту строк, что повышает читабельность таблицы.

![table12.tex](image05/image_17_1.png){ width=70% }

![table12.pdf](image05/image_17_2.png){ width=70% }

# Выводы

Я изучил основные возможности LaTeX для создания и форматирования таблиц. Получены практические навыки использования пакетов *array*, *booktabs*, *tabularx*, *longtable*, *threeparttable* и *siunitx*. 
