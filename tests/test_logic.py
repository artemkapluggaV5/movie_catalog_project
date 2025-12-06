import unittest
from logic import add_movie, mark_watched, find_by_year, get_unwatched, load_movies, save_movies


class TestMovieLogic(unittest.TestCase):

    def setUp(self):
        self.movies = [
            {"id": 1, "title": "Test Movie 1", "year": 2000, "watched": False, "rating": None},
            {"id": 2, "title": "Test Movie 2", "year": 2023, "watched": True, "rating": 8}
        ]

    def test_add_movie(self):
        add_movie(self.movies, "New Movie", 2024)
        self.assertEqual(len(self.movies), 3)
        self.assertEqual(self.movies[-1]["title"], "New Movie")
        self.assertEqual(self.movies[-1]["id"], 3)

    def test_add_movie_to_empty_list(self):
        empty = []
        add_movie(empty, "First", 1990)
        self.assertEqual(len(empty), 1)
        self.assertEqual(empty[0]["id"], 1)

    def test_mark_watched_simple(self):
        mark_watched(self.movies, 1)
        self.assertTrue(self.movies[0]["watched"])
        self.assertIsNone(self.movies[0]["rating"])

    def test_mark_watched_with_rating(self):
        mark_watched(self.movies, 1, 10)
        self.assertTrue(self.movies[0]["watched"])
        self.assertEqual(self.movies[0]["rating"], 10)

    def test_mark_watched_invalid_rating(self):
        mark_watched(self.movies, 1, 99)
        self.assertTrue(self.movies[0]["watched"])
        self.assertIsNone(self.movies[0]["rating"])

    def test_find_by_year(self):
        result = find_by_year(self.movies, 2023)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["title"], "Test Movie 2")

    def test_find_by_year_not_found(self):
        result = find_by_year(self.movies, 1800)
        self.assertEqual(result, [])

    def test_get_unwatched(self):
        unwatched = get_unwatched(self.movies)
        self.assertEqual(len(unwatched), 1)
        self.assertEqual(unwatched[0]["id"], 1)


if __name__ == '__main__':
    unittest.main()