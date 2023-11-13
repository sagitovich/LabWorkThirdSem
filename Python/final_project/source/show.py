import csv, random 

def show(data, type_output, count_rows, separator):

    if len(data) == 0:
        print('Файл не содержит данных')
        exit()

    if count_rows > len(data):
        count_rows = len(data)
        print(f'Число строк в файле меньше, чем заданных. Выводим все {count_rows} строк.')

    if type_output == 'top':
        row_indices = data[1:count_rows+1]
        # берём срез от одного до конца
    elif type_output == 'botton':
        row_indices = data[-count_rows:]
    elif type_output == 'random':
        row_indices = random.sample(data[1:], count_rows)
    else:
        print('TypeOutputError')

    column_width = [max(len(item) for item in column) for column in zip(*data)]

    headers = data[0]
    formated_headers = [item.ljust(width) for item, width in zip(headers, column_width)]
    print(separator.join(formated_headers))

    for index in row_indices:
        formated_row = [item.ljust(width) for item, width in zip(index, column_width)]
        print(separator.join(formated_row))
        
    