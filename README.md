#### Homework1
Код для парсинга данных расстрельных списков с сайта https://bessmertnybarak.ru/
#### Входные данные: 
ссылка на расстрельный список, аргумент -indir
#### Выходные данные:
Excel-файл со следующими колонками:
1. ФИО расстрелянного;
2. Дата приговора;
3. Дата расстрела;
3. ФИО и звание палача;
4. Уровень образования палача;
5. Кто присутствовал (в приговоре бывает раздел ПРИСУТСТВОВАЛИ, нужно его содержимое);
6. ФИО и должность/звание подписавшего приговор;
7. Организация, предоставившая информацию о расстрельном списке.
Если информация в списке отсутствует, в таблицу записывается NaN

Пример датафрейма с результатом парсинга расстрельного списка Бутовского полигона от 2-го января 1938-го года: https://bessmertnybarak.ru/article/2_yanvarya_1938_goda/
https://drive.google.com/file/d/1Q6Vbqc5blE963If0eJNLsTbQjNnOUazt/view?usp=sharing
