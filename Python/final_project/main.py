from source.loader import *
from source.show import *
from source.info import *
from source.delNan import *
from source.makeDS import *

file_path = 'data.csv'
data = load_csv(file_path)

type_output = input('Введите тип вывода: ')
count = input('Введите количество выводимых строк: ')
separator = input('Введите тип разделения: ')

if not type_output:
    type_output = 'top' 
if not count:
    count = 5
else:
    count = int(count)
if not separator:
    separator = '       '

# statistic_info(data)
# data = delete_empty_row(data)
# show(data, type_output, count, separator)
split_data(data)
