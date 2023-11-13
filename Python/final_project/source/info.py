def statistic_info(data):
    
    count_rows = 0
    for row in data:
        if any(row):
            count_rows += 1

    count_columns = 0
    for column in data[0]:
        if any(column):
            count_columns += 1

    print(f'Размерность таблицы с данными: {count_rows}x{count_columns}')

    #######################

    headers = data[0]
    field_info = {}
    for row in data[1:]:
        for i, value in enumerate(row):
            if value:
                field = headers[i]
                if field not in field_info:
                    field_info[field] = {'count':0, 'types':set()}
                field_info[field]['count'] += 1
                field_info[field]['types'].add(type(value).__name__)

    for field, info in field_info.items():
        count = info['count']
        types = ', '.join(info['types'])
        print(field, count, types)
