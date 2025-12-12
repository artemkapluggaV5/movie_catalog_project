import json


def load_movies(path: str) -> list[dict]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_movies(path: str, movies: list[dict]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(movies, f, ensure_ascii=False, indent=4)


def add_movie(movies: list[dict], title: str, year: int) -> list[dict]:
    if year < 0:
        raise ValueError("Год не может быть отрицательным")

    if check_movie_exists(movies, title, year):
        raise ValueError("Такой фильм уже существует")

    new_id = max((m["id"] for m in movies), default=0) + 1

    movies.append({
        "id": new_id,
        "title": title,
        "year": year,
        "watched": False
    })
    return movies


def mark_watched(movies: list[dict], movie_id: int) -> list[dict]:
    if movie_id < 0:
        raise ValueError("ID не может быть отрицательным")

    found = False
    for movie in movies:
        if movie["id"] == movie_id:
            movie["watched"] = True
            found = True
            break

    if not found:
        raise ValueError(f"Фильм с ID {movie_id} не найден.")

    return movies


def find_by_year(movies: list[dict], year: int) -> list[dict]:
    if year < 0:
        raise ValueError("Год не может быть отрицательным")

    return [m for m in movies if m["year"] == year]


def check_movie_exists(movies, title, year):
    return any(m["title"] == title and m["year"] == year for m in movies)


def format_movie(movie: dict) -> str:
    status = "Просмотрен" if movie["watched"] else "Не просмотрен"
    return f"[{movie['id']}] {movie['title']} ({movie['year']}) - {status}"
