Приложение реализующее решение задач <a>методов поисковой оптимизации</a>.
Программа включает в себя решение 8 алгоритмов на заданных функциях.

<h3 align="center"> Алгоритмы и функции </h3>
<table>
    <ol><a>Алгоритмы оптимизации:</a></ol>
    <tr>
        <li>Градиентный спуск</li>
        <li>Квадратичное программирование</li>
        <li>Функция Розенброкка</li>
        <li>Рой частиц</li>
        <li>Пчелинная оптимизация</li>
        <li>Исскуственная имунная сеть</li>
        <li>Бактериальная оптимизация</li>
        <li>Гибридный алгоритм (возможен) </li>
    </tr>
    <ol><a>Оптимизируемые функции:</a></ol>
    <tr>
        <li>Функция Химмельблау</li>
        <li>Функция сферы</li>
        <li>Функция Матьяса</li>
        <li>Функция Изома</li>
        <li>Функция Экли</li>
        <li>Табличная функция Хольдера</li>
    </tr>
</table>
<h3 align="center"> Структура проекта </h3>
Архитектура проекта представляет из себя:

    < PROJECT ROOT >
       |
       |-- bin/                            
       |    |-- application.py              # Файл запуска
       |    |
       |    |-- data/                   
       |    |    |-- algorithms/            # Пакет с алгоритмами
       |    |    |
       |    |    |-- base/                  # Папка с основными файлами программы
       |    |    |    |-- layouts/          # Папка для StackedLayoutl (legacy) 
       |    |    |    |-- widgets/          # Пакет с виджетами отрисовки окна
       |    |    |    |-- MainWindow.py     # Главное окно
       |    |    |    |-- settings.txt      # Конфиг (legacy)
       |    |    |
       |    |    |-- functions/             # Пакет с функциями, для отрисовки
       |    |    |
       |    |    |-- images/                # Иконки
       |        
       |-- ************************************************************************
