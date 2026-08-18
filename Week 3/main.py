"""
main.py
--------
Entry point of the Recommendation System (Project 3).

Run this file to start the interactive command-line application:
    python main.py

The user can:
    1. Get recommendations by selecting genres/interests from a list.
    2. Get recommendations by typing free-text keywords.
    3. View all available movies in the dataset.
    4. Exit the application.
"""

from data import MOVIES
from recommender import RecommendationEngine


def print_header(title):
    print("\n" + "=" * 55)
    print(title.center(55))
    print("=" * 55)


def display_recommendations(results, mode="genre"):
    if not results:
        print("\nNo matching recommendations found. Try different input.\n")
        return

    print(f"\nTop {len(results)} Recommendation(s):\n")
    print(f"{'#':<3}{'Title':<26}{'Genres':<28}{'Rating':<8}{'Match Score'}")
    print("-" * 90)

    for index, (movie, score, extra) in enumerate(results, start=1):
        genres_str = ", ".join(movie["genres"])
        print(f"{index:<3}{movie['title']:<26}{genres_str:<28}{movie['rating']:<8}{score}")
    print()


def choose_genres(engine):
    all_genres = engine.get_all_genres()

    print("\nAvailable Genres:")
    for i, genre in enumerate(all_genres, start=1):
        print(f"  {i}. {genre}")

    print("\nEnter the numbers of your favourite genres, separated by commas.")
    print("Example: 1,4,7")
    user_input = input("Your choice: ").strip()

    selected = []
    for part in user_input.split(","):
        part = part.strip()
        if part.isdigit():
            idx = int(part)
            if 1 <= idx <= len(all_genres):
                selected.append(all_genres[idx - 1])

    if not selected:
        print("\nNo valid genres selected. Please try again.")
        return None

    print(f"\nSelected interests: {', '.join(selected)}")
    return selected


def choose_keywords():
    print("\nEnter a few interests/keywords describing what you like to watch.")
    print("Example: dragon, king, war  OR  space, astronaut, future")
    user_input = input("Your keywords: ").strip()
    return user_input.split(",")


def show_all_movies():
    print_header("ALL AVAILABLE MOVIES")
    print(f"{'Title':<26}{'Genres':<28}{'Year':<6}{'Rating'}")
    print("-" * 70)
    for movie in MOVIES:
        genres_str = ", ".join(movie["genres"])
        print(f"{movie['title']:<26}{genres_str:<28}{movie['year']:<6}{movie['rating']}")
    print()


def main():
    engine = RecommendationEngine(MOVIES)

    while True:
        print_header("MOVIE RECOMMENDATION SYSTEM")
        print("1. Recommend by selecting genres")
        print("2. Recommend by typing keywords/interests")
        print("3. View all movies")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            selected_genres = choose_genres(engine)
            if selected_genres:
                results = engine.recommend_by_genres(selected_genres, top_n=5)
                display_recommendations(results, mode="genre")

        elif choice == "2":
            keywords = choose_keywords()
            results = engine.recommend_by_keywords(keywords, top_n=5)
            display_recommendations(results, mode="keyword")

        elif choice == "3":
            show_all_movies()

        elif choice == "4":
            print("\nThank you for using the Recommendation System. Goodbye!\n")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.\n")


if __name__ == "__main__":
    main()
