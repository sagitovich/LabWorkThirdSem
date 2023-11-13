import hashlib

def hash_text(text):
    # Выбираем хеш-функцию (например, hashlib.sha256)
    hasher = hashlib.sha256()
    hasher.update(text.encode())
    return hasher.hexdigest()

def pizdec():
    with open('/Users/a.sagitovich/programming/BFU/ASD/13/english_text.txt', "r", encoding="utf-8") as file:
        lines = file.readlines()

    hash_table = {}

    for i, line in enumerate(lines, start=1):
        words = line.split()

        for word in words:
            # Удаление знаков препинания в конце слова
            word = word.strip('.,:;!?)-')

            # Если слово не пустое, добавляем его в соответствующий список в хеш-таблице
            if word:
                word_length = len(word)

                if word_length not in hash_table:
                    hash_table[word_length] = []

                hash_table[word_length].append((i, word))

    # Вычисляем хеши для списков слов одинаковой длины
    hash_values = {}
    for word_length, word_list in hash_table.items():
        combined_words = [word for _, word in word_list]
        hash_value = hash_text(" ".join(combined_words))
        hash_values[word_length] = hash_value

    # Вывод результата на экран
    for word_length, word_list in hash_table.items():
        print(f"Key: {word_length}")
        for word in word_list:
            print(f"Value: {word}\nHash: {hash_values[word_length]}")
        print()

pizdec()