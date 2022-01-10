import os
import shutil
import uuid

DIR = os.path.dirname(os.path.abspath(__file__))
DIR_DATA = f"{DIR}/library/"

class Book():

    def __init__(self, books):
        self.books = books
        self.chapter = 0
        self._create_folder_book()

    #подсчет кол-во глав в книги
    def number_of_chapters(self, file_books):
        return len(os.listdir('library/' + file_books + '/Главы/'))

    #изменение кол-во глав
    def _change_the_number_of_chapters(self):
        with open ('library/' + self.books + '/info.txt', 'r', encoding='utf-8') as f:
            line = f.readlines()
            line_one = line[0]
            line[1] = 'Количество глав в книги:'

            new_data = line[1].replace('Количество глав в книги:',
                                f'Количество глав в книги:{str(self.number_of_chapters(self.books))}')

            self.overwriting_data_in_info_txt(line_one, new_data)

    def _create_folder_book(self):
            #Создание папки/книги
        os.makedirs('library' + '/' + self.books + '/Главы')
        self.create_file_in_filder_book()
        self.add_unic_id_in_book_filder()

    def create_file_in_filder_book(self):
        # Создание файла в этой же папки
        info_folder = 'library' + '/' + self.books + '/info.txt'
        file = open(info_folder, 'w', encoding='utf-8')
        file.close()

    def add_unic_id_in_book_filder(self):
        # #В этом файле записываем уникальный id и сколько глав в книги
        book_information = f'library/{self.books}/info.txt'
        id = uuid.uuid4()
        if self.books in book_information:
            with open(book_information, "w", encoding="utf-8") as file_book_info:
                file_book_info.write(f"Ваш уникальный id: {id}\
                                        \nКоличество глав в книги:0")

    #перезапись данных в info.txt            
    def overwriting_data_in_info_txt(self,
                        first_line, second_line):

        with open ('library/' + self.books + '/info.txt', 'w', encoding='utf-8') as f:
                f.write(first_line + second_line)
        
    #Создание главы/файла в книги
    def chapter_of_the_book(self, chapter_title):
        file = open('library/' + self.books + '/Главы/' + chapter_title, 'w', encoding='utf-8')
        file.close()
        self._change_the_number_of_chapters()

    def create_chapter(self):
        self.chapter +=1
        self._change_the_number_of_chapters()

    def delete_chapter(self):
        self.count_chapters -= 1
        self._change_the_number_of_chapters()
        
class Library:
    
    @staticmethod
    def get_all_books():
        # Получаем все книги
        books = []
        for file_name in os.listdir(DIR_DATA):
            books.append(file_name)
        return books

    def __init__(self, books):
        self.books = books

class LibraryInterface:
    def __init__(self, books):
        self.books = books

    # Вывести информацию о всех существующих книгах
    def display_information_about_all_books(self):
        for book in self.books:
            print(f'\nКнига"{book}"')
            file_group = open(f'library/{book}/info.txt', 'r', encoding='utf-8')
            print(file_group.read())
            file_group.close()




print("Добро пожаловать в приложение по созданию электронной библеотеки")

new_book = Book(input('Введите название книги\n'))


while True:
    print("""
        У вас есть возможности:
        1.Добавление глав к книге
        2.Удаление книги
        3.Изменить название книги
        4.Изменить название главы
        5.Удалить главу
        6.Вывести информацию о всех существующих книгах
        7.Выйти из программы
    """)
    user_choice = input('Напишите ,что вы хотите сделать\n')

    lib_int = LibraryInterface(Library.get_all_books())
    library = Library(lib_int)
    

    if user_choice == '1':

        chapter_book = input('Напишите название главы для этой книги\n')
        new_book.chapter_of_the_book(chapter_book)
        new_book.create_chapter()
        print('Вы успешно добавили главу!')

    elif user_choice == '2':
        user_book = input('Введите название книги для ее удаления:\n')

        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), user_book)
        shutil.rmtree(f'library/{user_book}')
        print('Вы успешно удалили книгу!')
        break

    elif user_choice == '3':
        #переименование книги
        old_name_book = input('Введите название книги в которую хотите переименовать\n')
        new_name_book = input('Введите новое название\n')

        old_name = f'library/{old_name_book}/'
        new_name = f'library/{new_name_book}/'
        os.rename(old_name, new_name)
        print('Вы успешно изменили название на "{0}"!'.format(new_name_book))
        
    elif user_choice == '4':
        #переименование главы
        user_book = input('Введите название книги,в которой хотите изменить название главы:\n')
        
        print('Все главы в этой книги')
        for i in os.listdir('library/'+ user_book + '/Главы'):
            print(i)
        
        os.chdir('library/' + user_book + '/Главы/')
        old_name_book = input('Введите название главы которое хотите изменить\n')
        new_name_book = input('Введите новое название главы\n')
        
        os.rename(old_name_book, new_name_book)
        print('Вы успешно изменили название на "{0}" !'.format(new_name_book))
    
    elif user_choice == '5':
        #Удаление главы из книги

        user_book = input('Введите название Книги\n')
        print('Все главы в этой книги')
        for i in os.listdir('library/' + user_book + '/Главы'):
            print(i)
        
        del_book_chapter = input('Введите главу\n')
        os.remove('library/' + user_book + '/Главы/' + del_book_chapter)

        print('Все главы в этой книги')
        for i in os.listdir('library/' + user_book + '/Главы'):
            print(i)
        
        print('Вы успешно удалили главу "{0}"!'.format(del_book_chapter))
        new_book.delete_chapter()

    elif  user_choice == '6':  
        lib_int.display_information_about_all_books()
    
    elif user_choice == '7':
        print('Вы вышли из программы')
        break

    # else:
    #     print('Не допустимый ввод')
    #     continue