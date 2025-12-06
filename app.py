import logic

FILENAME = "movies.json"


def print_movie(movie):
    status = "Просмотрен" if movie['watched'] else "Не просмотрен"
    rating = f", Рейтинг: {movie['rating']}" if movie['rating'] else ""
    print(f"[{movie['id']}] {movie['title']} ({movie['year']}) - {status}{rating}")


def run_app():
    movies = logic.load_movies(FILENAME)
    print("Добро пожаловать в Каталог Фильмов!")

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Показать все фильмы")
        print("2. Показать непросмотренные фильмы")
        print("3. Добавить фильм")
        print("4. Отметить фильм как просмотренный (с оценкой или без)")
        print("5. Найти фильмы по году")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            if not movies:
                print("Список пуст.")
            else:
                for m in movies:
                    print_movie(m)

        elif choice == '2':
            unwatched = logic.get_unwatched(movies)
            if not unwatched:
                print("Все фильмы просмотрены!")
            else:
                for m in unwatched:
                    print_movie(m)

        elif choice == '3':
            title = input("Введите название фильма: ")
            try:
                year = int(input("Введите год выпуска: "))
                logic.add_movie(movies, title, year)
                logic.save_movies(FILENAME, movies)
                print("Фильм успешно добавлен!")
            except ValueError:
                print("Ошибка: Год должен быть числом.")

        elif choice == '4':
            try:
                m_id = int(input("Введите ID фильма: "))
                rating_input = input("Оценка (1-10) или Enter, если без оценки: ")
                rating = int(rating_input) if rating_input else None

                logic.mark_watched(movies, m_id, rating)
                logic.save_movies(FILENAME, movies)
                print("Статус обновлен!")
            except ValueError:
                print("Ошибка: ID и оценка должны быть числами.")

        elif choice == '5':
            try:
                year = int(input("Введите год для поиска: "))
                found = logic.find_by_year(movies, year)
                if found:
                    for m in found:
                        print_movie(m)
                else:
                    print("Фильмов этого года не найдено.")
            except ValueError:
                print("Ошибка: введите корректный год.")

        elif choice == '0':
            print("До свидания!")
            break

        else:
            print("Неверный пункт меню.")


if __name__ == '__main__':
    run_app()