import csv 

def load_csv(path):
    list_ = []                          # список для всех данных
    with open(path, 'r') as file:       # открываем файл для чтения
        csv_reader = csv.reader(file)   # считываем csv файл в переменную
    
        list_ = list(csv_reader)        # конвертируем данные из переменной в список

    return list_ 

