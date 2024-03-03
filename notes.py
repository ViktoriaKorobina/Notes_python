import json
from datetime import datetime

def save_notes(notes):
    try:
        with open('notes.json', 'w') as f:
            json.dump(notes, f)
    except Exception as e:
        print(f'Ошибка при сохранении заметок: {e}')

def read_notes():
    try:
        with open('notes.json') as f:
            notes = json.load(f)
        return notes
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f'Ошибка при чтении заметок: {e}')
        return []

def add_note(title, message):
    notes = read_notes()
    note = {
        'id': len(notes) + 1,
        'title': title,
        'message': message,
        'created': datetime.now().strftime('%d.%m.%Y'),
        'updated': None
    }
    notes.append(note)
    save_notes(notes)
    return 'Заметка успешно добавлена!'

def edit_note(id, title, message):
    notes = read_notes()
    for note in notes:
        if note['id'] == id:
            note['title'] = title
            note['message'] = message
            note['updated'] = datetime.now().strftime('%d.%m.%Y')
            save_notes(notes)
            return 'Примечание успешно отредактировано!'
    return 'Не удалось найти заметку!'

def delete_note(id):
    notes = read_notes()
    note_to_delete = None
    for note in notes:
        if note['id'] == id:
            note_to_delete = note
            break
    if note_to_delete:
        notes.remove(note_to_delete)
        save_notes(notes)
        return f'Заметка {id} удалена!'
    else:
        return 'Заметка не найдена!'

def filter_by_date(start_date, end_date):
    filtered_notes = []
    for note in read_notes():
        created_date = datetime.strptime(note['created'], '%d.%m.%Y')
        updated_date = created_date
        if note['updated']:
            updated_date = datetime.strptime(note['updated'], '%d.%m.%Y')
        if start_date <= created_date <= end_date or start_date <= updated_date <= end_date:
            filtered_notes.append(note)
    return filtered_notes

def print_notes():
    notes = read_notes()
    for note in notes:
        print(note)

def show_note(id):
    int_id = int(id)
    notes = read_notes()
    for note in notes:
        if note['id'] == int_id:
            print(note)
def main():
    print('Введите команду (add, edit, delete, filter, print, show, exit). Для выхода введите "exit".')
    while True:
        command = input('Введите команду: ')
        if command == 'add':
            title = input('Заголовок заметки: ')
            message = input('Тело заметки: ')
            print(add_note(title, message))
        elif command == 'edit':
            id = int(input('ID заметки: '))
            title = input('Новый заголовок заметки: ')
            message = input('Новое тело заметки: ')
            print(edit_note(id, title, message))
        elif command == 'delete':
            id = int(input('ID заметки для удаления: '))
            print(delete_note(id))
        elif command == 'filter':
            start_date = datetime.strptime(input('Начальная дата (ДД.ММ.ГГГ): '), '%d.%m.%Y')
            end_date = datetime.strptime(input('Конечная дата (ДД.ММ.ГГГГ): '), '%d.%m.%Y')
            filtered_notes = filter_by_date(start_date, end_date)
            for note in filtered_notes:
                print(note)
        elif command == 'print':
            print_notes()
        elif command == 'show':
            show_note(input('Введите ID: '))
        elif command.lower() == 'exit':
            break

main()