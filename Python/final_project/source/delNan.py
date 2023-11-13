def delete_empty_row(data):
    
    print(f'Количество строк до удаления пустых строк: {len(data[1:])}')
    data = [row for row in data if any(row)]
    print(f'Количество строк после удаления пустых строк: {len(data[1:])}')

    return data