import json

def load_movies(path: str) -> list[dict]:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_movies(path: str, movies: list[dict]) -> None:
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(movies, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")

def add_movie(movies: list[dict], title: str, year: int) -> list[dict]:
    if not movies:
        new_id = 1
    else:
        last_movie = movies[-1]
        new_id = last_movie['id'] + 1

    new_movie = {
        "id": new_id,
        "title": title,
        "year": year,
        "watched": False,
        "rating": None
    }
    movies.append(new_movie)
    return movies

def mark_watched(movies: list[dict], movie_id: int, rating: int | None = None) -> list[dict]:
    for movie in movies:
        if movie['id'] == movie_id:
            movie['watched'] = True
            if rating is not None and 1 <= rating <= 10:
                movie['rating'] = rating
    return movies

def find_by_year(movies: list[dict], year: int) -> list[dict]:
    found = []
    for movie in movies:
        if movie['year'] == year:
            found.append(movie)
    return found

def get_unwatched(movies: list[dict]) -> list[dict]:
    found = []
    for movie in movies:
        if not movie['watched']:
            found.append(movie)
    return found