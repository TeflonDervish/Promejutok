import os
from datetime import datetime

class Note:
    def __init__(self, id, title, message, timestamp):
        self.id = id
        self.title = title
        self.message = message
        self.timestamp = timestamp

    def __str__(self):
        return f"ID: {self.id}, Заголовок: {self.title}, Текст: {self.message}, Дата/время: {self.timestamp}"

class NoteManager:
    def __init__(self, filename):
        self.filename = filename
        self.notes = self.load_notes()

    def load_notes(self):
        notes = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(';')
                    notes.append(Note(int(parts[0]), parts[1], parts[2], parts[3]))
        except FileNotFoundError:
            pass
        return notes

    def save_notes(self):
        with open(self.filename, 'w') as file:
            for note in self.notes:
                file.write(f"{note.id};{note.title};{note.message};{note.timestamp}\n")

    def add_note(self, title, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        note = Note(len(self.notes) + 1, title, message, timestamp)
        self.notes.append(note)
        self.save_notes()
        print("Заметка успешно сохранена.")

    def list_notes(self):
        if self.notes:
            for note in self.notes:
                print(note)
        else:
            print("Список заметок пуст.")

    def edit_note(self, note_id, new_title, new_message):
        for note in self.notes:
            if note.id == note_id:
                if new_title:
                    note.title = new_title
                if new_message:
                    note.message = new_message
                note.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_notes()
                print("Заметка успешно отредактирована.")
                return
        print("Заметка с указанным ID не найдена.")

    def delete_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                self.notes.remove(note)
                self.save_notes()
                print("Заметка успешно удалена.")
                return
        print("Заметка с указанным ID не найдена.")

if __name__ == "__main__":
    filename = "notes.txt"
    manager = NoteManager(filename)

    while True:
        print("\nМеню:")
        print("1. Просмотреть заметки")
        print("2. Добавить заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            manager.list_notes()
        elif choice == '2':
            title = input("Введите заголовок заметки: ")
            message = input("Введите текст заметки: ")
            manager.add_note(title, message)
        elif choice == '3':
            note_id = int(input("Введите ID заметки для редактирования: "))
            new_title = input("Введите новый заголовок (оставьте пустым, чтобы оставить без изменений): ")
            new_message = input("Введите новый текст (оставьте пустым, чтобы оставить без изменений): ")
            manager.edit_note(note_id, new_title, new_message)
        elif choice == '4':
            note_id = int(input("Введите ID заметки для удаления: "))
            manager.delete_note(note_id)
        elif choice == '5':
            print("До свидания!")
            break
        else:
            print("Некорректный ввод. Попробуйте ещё раз.")
