import unittest
from movie.rest_api.movie_resource import MovieResource, MovieCreateResource, MovieListResource
from movie.domain.movie import Movie
from unittest.mock import patch


class TestMovieCreateResource(unittest.TestCase):
    @patch('movie.rest_api.movie_resource.MovieRepository')
    def test_post(self, mock_movie):
        mock_movie.return_value.create.return_value = "123"
        mr = MovieCreateResource()
        res = mr.post()
        self.assertEqual(res.status_code, 201)


class TestMovieResource(unittest.TestCase):
    @patch('movie.rest_api.movie_resource.MovieRepository')
    def test_get_right(self, mock_movie):
        movie = Movie(name='a', description='b', length=90, movie_id="123")
        mock_movie.return_value.get.return_value = movie
        mr1 = MovieResource()
        res = mr1.get('123')
        self.assertEqual(res.status_code, 200)

    def test_get_error(self):
        mr = MovieResource()
        try:
            res = mr.get("5bd0a351")
        except:
            self.assertTrue(True)

    def test_delete_error(self):
        mr = MovieResource()
        try:
            res = mr.delete("5bd0a351")
        except:
            self.assertTrue(True)

    @patch('movie.rest_api.movie_resource.MovieRepository')
    def test_delete_right(self, mock_movie):
        mock_movie.return_value.delete.return_value = ''
        mr1 = MovieResource()
        res = mr1.delete('123')
        self.assertEqual(res.status_code, 204)


class TestMovieListResource(unittest.TestCase):
    @patch('movie.rest_api.movie_resource.MovieRepository')
    def test_get(self, mock_movie):
        movies = []
        movie = Movie(name='movie', description='description', length=60, movie_id="123")
        movies.append(movie)
        mock_movie.return_value.read_paginated.return_value = movies, False, True
        mr = MovieListResource()
        res = mr.get()
        self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main()
