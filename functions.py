def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{fio} | {phone}')

def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    print(data)
    data_to_find = input('Введите данные для поиска: ')
    print(search(data, data_to_find))

def search(book: str, info: str) -> str:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.splitlines()
    results = []
    for contact in book:
        if info in contact:
            results.append(contact)
    if len(results)>1:
        results = "\n".join(results)
        print(results)
        print("уточните критерий поиска")
        newinfo = input()
        return search(results, newinfo)
    if len(results)==1:
        return "\n".join(results)
    return 'Совпадений не найдено'

def edit_data():
    """Позволяет изменить или удалить строку из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    print(data)
    data_to_find = input('Введите данные для поиска редактируемой строки: ')
    old_string = search(data, data_to_find)
    print("введите новые данные или оставьте строку пустой для удаления")
    new_string = input()
    new_data = data.replace(old_string, new_string)
    new_data = "".join([s for s in new_data.strip().splitlines(True) if s.strip()])
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write(new_data)


