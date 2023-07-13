Иерархия ошибок и исключений в Python
![Иерархия ошибок и исключений в Python](https://raw.githubusercontent.com/PitKoro/MAI-python-1-course/e6b8dbab951f68fb77f35d1e32d2deda32f1f11d/img/exeption.png)

# Домашнее задание 1. 
* Реализуйте 3 метода, чтобы в каждом из них получить разные исключения

[Решение](https://github.com/JuliaRyzhova/Errors-and-Exceptions/tree/master/home_work_1) 


# Домашнее задание 2.

1. Реализуйте метод, который запрашивает у пользователя ввод дробного числа (типа float), и возвращает введенное значение. Ввод текста вместо числа не должно приводить к падению приложения, вместо этого, необходимо повторно запросить у пользователя ввод данных.

[Решение](https://github.com/JuliaRyzhova/Errors-and-Exceptions/blob/master/home_work_2/task_1.py)

2. Если необходимо, исправьте данный код

[По этой ссылке](https://docs.google.com/document/d/17EaA1lDxzD5YigQ5OAal60fOFKVoCbEJqooB9XfhT7w/edit)

[Решение](https://github.com/JuliaRyzhova/Errors-and-Exceptions/blob/master/home_work_2/task_2.py)

3. Дан следующий код, исправьте его там, где требуется

[По этой ссылке](https://docs.google.com/document/d/17EaA1lDxzD5YigQ5OAal60fOFKVoCbEJqooB9XfhT7w/edit)

[Решение](https://github.com/JuliaRyzhova/Errors-and-Exceptions/blob/master/home_work_2/task_3.py)

4. Разработайте программу, которая выбросит Exception, когда пользователь вводит пустую строку. Пользователю должно показаться сообщение, что пустые строки вводить нельзя!!!

[Решение](https://github.com/JuliaRyzhova/Errors-and-Exceptions/blob/master/home_work_2/task_4.py)

# Домашнее задание 3.
Напишите приложение, которое будет запрашивать у пользователя следующие данные, разделенные пробелом: Фамилия Имя Отчество датарождения номертелефона пол Форматы данных: фамилия, имя, отчество - строки

дата_рождения - строка формата dd.mm.yyyy

номер_телефона - целое беззнаковое число без форматирования

пол - символ латиницей f или m.

Приложение должно проверить введенные данные по количеству. Если количество не совпадает с требуемым, вернуть код ошибки, обработать его и показать пользователю сообщение, что он ввел меньше и больше данных, чем требуется.

Приложение должно попытаться распарсить полученные значения и выделить из них требуемые параметры. Если форматы данных не совпадают, нужно бросить исключение, соответствующее типу проблемы. Можно использовать встроенные типы java и создать свои. Исключение должно быть корректно обработано, пользователю выведено сообщение с информацией, что именно неверно.

Если всё введено и обработано верно, должен создаться файл с названием, равным фамилии, в него в одну строку должны записаться полученные данные, вида

<Фамилия><Имя><Отчество><датарождения> <номертелефона><пол>

Однофамильцы должны записаться в один и тот же файл, в отдельные строки.

Не забудьте закрыть соединение с файлом.

При возникновении проблемы с чтением-записью в файл, исключение должно быть корректно обработано, пользователь должен увидеть стектрейс ошибки.

[Решение](https://github.com/JuliaRyzhova/Errors-and-Exceptions/blob/master/home_work_3/main.py)#   g b _ e x c e p t i o n  
 #   g b _ e x c e p t i o n  
 #   g b _ e x c e p t i o n  
 #   g b _ e x c e p t i o n  
 