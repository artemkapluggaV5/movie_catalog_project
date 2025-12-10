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
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(movies, f, ensure_ascii=False, indent=4)
    except OSError:
        pass


def add_movie(movies: list[dict], title: str, year: int) -> list[dict]:
    if not movies:
        new_id = 1
    else:
        new_id = max(movie["id"] for movie in movies) + 1

    new_movie = {
        "id": new_id,
        "title": title,
        "year": year,
        "watched": False
    }

    movies.append(new_movie)
    return movies


def mark_watched(movies: list[dict], movie_id: int) -> list[dict]:
    for movie in movies:
        if movie["id"] == movie_id:
            movie["watched"] = True
            break
    return movies


def find_by_year(movies: list[dict], year: int) -> list[dict]:
    result = []
    for movie in movies:
        if movie.get("year") == year:
            result.append(movie)
    return result
