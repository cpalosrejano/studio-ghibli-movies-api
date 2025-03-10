import importlib
from typing import List
from app.data.schema import Movie


# function to translate a list of movies to a lang
def translate_movies(movies: List[Movie], lang: str) :
    translations = movie_translations_for(lang)

    for movie in movies:
        # check if the movie has translation
        if movie.title in translations:
            translation = translations[movie.title]
            # update title and description
            movie.title = translation.title
            movie.description = translation.description

    return movies


# function to fetch the movie translator
def movie_translations_for(lang: str):
    try:
        # try to load desired lang
        translation_module = importlib.import_module(f"app.translations.movie.{lang}")
        return translation_module.translations
    except ModuleNotFoundError:
        # if lang is not defined, try to return english lang as default
        try:
            translation_module = importlib.import_module("app.translations.movie.en")
            return translation_module.translations
        except ModuleNotFoundError:
            # if english is not defined, return empty map
            return {}
