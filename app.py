from logic import load_movies, save_movies, add_movie, mark_watched, find_by_year

DATA_FILE = "movies.json"

def print_movie(movie):
    status = "Просмотрен" if movie["watched"] else "Не просмотрен"
    print(f"[{movie['id']}] {movie['title']} ({movie['year']}) - {status}")

def run_app():
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
            if movies:
                for m in movies:
                    print_movie(m)
            else:
                print("Список пуст.")

        elif choice == "2":
            title = input("Введите название фильма: ")
            try:
                year = int(input("Введите год выпуска: "))
                add_movie(movies, title, year)
                save_movies(DATA_FILE, movies)
                print("Фильм добавлен!")
            except ValueError:
                print("Год должен быть числом.")

        elif choice == "3":
            try:
                m_id = int(input("Введите ID фильма: "))
                mark_watched(movies, m_id)
                save_movies(DATA_FILE, movies)
                print("Статус обновлён")
            except ValueError:
                print("ID должен быть числом.")

        elif choice == "4":
            try:
                year = int(input("Введите год: "))
                found = find_by_year(movies, year)
                if found:
                    for m in found:
                        print_movie(m)
                else:
                    print("Нет фильмов за этот год.")
            except ValueError:
                print("Год должен быть числом.")

        elif choice == "0":
            save_movies(DATA_FILE, movies)
            print("До свидания")
            break

        else:
            print("Неверный пункт меню.")

if __name__ == "__main__":
    run_app()
