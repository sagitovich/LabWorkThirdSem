import os, random, csv 

def split_data(data):
    ratio = 0.7      # соотношение

    headers = data[0]
    random.shuffle(data)                      # перемешиваем все данные
    size_education = int(len(data) * ratio)   # размер данных на файл "обучение"

    data_education = data[1:size_education+1]
    data_test = data[size_education+1:]

    folder_path = os.path.join(os.getcwd(), 'workdata')
    os.makedirs(folder_path, exist_ok=True)

    learning_path = os.path.join(folder_path, 'learning')
    os.makedirs(learning_path, exist_ok=True)

    education_file_path = os.path.join(learning_path, 'train.csv')
    with open (education_file_path, 'w', newline='') as education_file:
        csv_writer = csv.writer(education_file, delimiter=',')
        csv_writer.writerow(headers)
        csv_writer.writerows(data_education)

    testing_path = os.path.join(folder_path, 'testing')
    os.makedirs(testing_path, exist_ok=True)

    test_file_path = os.path.join(testing_path, 'test.csv')
    with open (test_file_path, 'w', newline='') as test_file:
        csv_writer = csv.writer(test_file, delimiter=',')
        csv_writer.writerow(headers)
        csv_writer.writerows(data_test)

