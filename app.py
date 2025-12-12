from logic import (
    load_movies, save_movies, show_all_movies,
    add_movie_interactive, mark_watched_interactive,
    find_by_year_interactive, print_movie
)

DATA_FILE = "movies.json"


def main():
    movies = load_movies(DATA_FILE)
    print("Добро пожаловать в Каталог Фильмов!")

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Показать все фильмы")
        print("2. Добавить фильм")
        print("3. Отметить фильм как просмотренный")
        print("4. Найти фильмы по году")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            show_all_movies(movies)

        elif choice == "2":
            title = input("Введите название фильма: ")
            year = input("Введите год выпуска: ")
            if add_movie_interactive(movies, title, year):
                save_movies(DATA_FILE, movies)
                print("Фильм добавлен!")
            else:
                print("Год должен быть положительным числом.")

        elif choice == "3":
            show_all_movies(movies)
            m_id = input("Введите ID фильма: ")
            if mark_watched_interactive(movies, m_id):
                save_movies(DATA_FILE, movies)
                print("Статус обновлён")
            else:
                print("ID должен быть числом.")

        elif choice == "4":
            year = input("Введите год: ")
            found = find_by_year_interactive(movies, year)
            if found:
                for m in found:
                    print_movie(m)
            else:
                print("Нет фильмов за этот год.")

        elif choice == "0":
            save_movies(DATA_FILE, movies)
            print("До свидания")
            break

        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()
