"""
recommender.py
----------------
Core logic of the Recommendation System.

This module implements a simple CONTENT-BASED recommendation engine using
two matching strategies:

1. Genre-based matching (Cosine Similarity)
   - The user selects genres/interests from a list.
   - Each movie's genres and the user's chosen genres are converted into
     binary vectors (one-hot style) over the full genre space.
   - Cosine similarity is calculated between the user vector and every
     movie vector to measure how closely they match.

2. Keyword-based matching (Pattern Matching)
   - The user types free-text interests/keywords (e.g. "dragon king war").
   - Each keyword is searched inside the movie's description + genres.
   - A match score is calculated based on how many keywords were found.

Both strategies produce a final ranked list of recommendations, using the
movie's rating as a small tie-breaker so that, among equally relevant
movies, better-rated ones are shown first.
"""

import math


class RecommendationEngine:
    def __init__(self, movies):
        """
        :param movies: list of movie dictionaries (see data.py)
        """
        self.movies = movies
        # Build the full set of unique genres available in the dataset
        self.all_genres = sorted({genre for movie in movies for genre in movie["genres"]})

    # ------------------------------------------------------------------
    # Helper: Vector building
    # ------------------------------------------------------------------
    def _build_vector(self, genres):
        """
        Convert a list of genres into a binary vector across all_genres.
        Example: if all_genres = [Action, Comedy, Drama]
                 and genres = [Comedy], vector = [0, 1, 0]
        """
        return [1 if genre in genres else 0 for genre in self.all_genres]

    # ------------------------------------------------------------------
    # Helper: Cosine similarity
    # ------------------------------------------------------------------
    @staticmethod
    def _cosine_similarity(vector_a, vector_b):
        """
        Cosine similarity = (A . B) / (||A|| * ||B||)
        Returns a value between 0 (no similarity) and 1 (perfect match).
        """
        dot_product = sum(a * b for a, b in zip(vector_a, vector_b))
        magnitude_a = math.sqrt(sum(a * a for a in vector_a))
        magnitude_b = math.sqrt(sum(b * b for b in vector_b))

        if magnitude_a == 0 or magnitude_b == 0:
            return 0.0

        return dot_product / (magnitude_a * magnitude_b)

    # ------------------------------------------------------------------
    # Strategy 1: Genre-based recommendation
    # ------------------------------------------------------------------
    def recommend_by_genres(self, selected_genres, top_n=5):
        """
        Recommend movies based on cosine similarity between the user's
        chosen genres and each movie's genres.

        Final score = 85% similarity + 15% normalized rating
        (rating acts as a tie-breaker between equally relevant movies)
        """
        user_vector = self._build_vector(selected_genres)
        scored_results = []

        for movie in self.movies:
            movie_vector = self._build_vector(movie["genres"])
            similarity = self._cosine_similarity(user_vector, movie_vector)

            if similarity > 0:
                normalized_rating = movie["rating"] / 10
                final_score = round((similarity * 0.85) + (normalized_rating * 0.15), 3)
                scored_results.append((movie, final_score, round(similarity, 3)))

        scored_results.sort(key=lambda item: item[1], reverse=True)
        return scored_results[:top_n]

    # ------------------------------------------------------------------
    # Strategy 2: Keyword-based recommendation (pattern matching)
    # ------------------------------------------------------------------
    def recommend_by_keywords(self, keywords, top_n=5):
        """
        Recommend movies based on how many user-given keywords appear
        inside the movie's description and genre tags.

        Final score = 90% keyword match ratio + 10% normalized rating
        """
        cleaned_keywords = [k.strip().lower() for k in keywords if k.strip()]
        if not cleaned_keywords:
            return []

        scored_results = []

        for movie in self.movies:
            searchable_text = (movie["description"] + " " + " ".join(movie["genres"])).lower()
            matches = sum(1 for keyword in cleaned_keywords if keyword in searchable_text)

            if matches > 0:
                match_ratio = matches / len(cleaned_keywords)
                normalized_rating = movie["rating"] / 10
                final_score = round((match_ratio * 0.90) + (normalized_rating * 0.10), 3)
                scored_results.append((movie, final_score, matches))

        scored_results.sort(key=lambda item: item[1], reverse=True)
        return scored_results[:top_n]

    # ------------------------------------------------------------------
    # Utility
    # ------------------------------------------------------------------
    def get_all_genres(self):
        return self.all_genres
