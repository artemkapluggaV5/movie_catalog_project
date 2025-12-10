from logic import load_movies, add_movie, mark_watched, find_by_year

def test_load_movies_empty():
    result = load_movies("file_which_does_not_exist.json")
    assert result == []

def test_add_movie():
    movies = []

    add_movie(movies, "Matrix", 1999)
    assert len(movies) == 1
    assert movies[0]["id"] == 1
    assert movies[0]["title"] == "Matrix"
    assert movies[0]["watched"] is False

    add_movie(movies, "Inception", 2010)
    assert movies[1]["id"] == 2

def test_mark_watched():
    movies = [
        {"id": 1, "title": "A", "year": 2000, "watched": False},
        {"id": 2, "title": "B", "year": 2001, "watched": False}
    ]

    mark_watched(movies, 2)
    assert movies[1]["watched"] is True

def test_find_by_year():
    movies = [
        {"id": 1, "title": "A", "year": 2000, "watched": False},
        {"id": 2, "title": "B", "year": 2000, "watched": False},
        {"id": 3, "title": "C", "year": 2021, "watched": False},
    ]

    found = find_by_year(movies, 2000)
    assert len(found) == 2

    not_found = find_by_year(movies, 1999)
    assert not_found == []
