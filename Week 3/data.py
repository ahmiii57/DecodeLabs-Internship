"""
data.py
--------
Sample dataset for the Recommendation System.

Each item (movie) has:
    - title       : Name of the movie
    - genres      : List of genres/tags associated with the movie
    - rating      : IMDb-style rating out of 10 (used as a quality tie-breaker)
    - year        : Release year
    - description : A short text description (used for keyword-based matching)

In a real-world project this data could come from a CSV file or a database.
For this project, it is kept in-memory to keep the system simple and easy
to run without any external setup.
"""

MOVIES = [
    {
        "title": "Galactic Frontier",
        "genres": ["Sci-Fi", "Adventure", "Action"],
        "rating": 8.2,
        "year": 2019,
        "description": "A crew of explorers travels beyond the solar system to find a new home for humanity."
    },
    {
        "title": "Laugh Riot",
        "genres": ["Comedy"],
        "rating": 7.1,
        "year": 2021,
        "description": "A clumsy office worker accidentally becomes the funniest stand-up comedian in the city."
    },
    {
        "title": "Silent Shadows",
        "genres": ["Thriller", "Mystery", "Crime"],
        "rating": 8.5,
        "year": 2018,
        "description": "A detective must solve a string of murders before the killer strikes again."
    },
    {
        "title": "Hearts Aligned",
        "genres": ["Romance", "Drama"],
        "rating": 7.6,
        "year": 2020,
        "description": "Two strangers meet on a train and slowly fall in love over one unforgettable night."
    },
    {
        "title": "The Last Kingdom Rises",
        "genres": ["Fantasy", "Adventure", "Action"],
        "rating": 8.8,
        "year": 2022,
        "description": "A young warrior must unite scattered kingdoms to defeat an ancient evil force."
    },
    {
        "title": "Haunted Hollow",
        "genres": ["Horror", "Thriller"],
        "rating": 6.9,
        "year": 2017,
        "description": "A family moves into an old house and discovers it holds a terrifying secret."
    },
    {
        "title": "Cartoon Kingdom",
        "genres": ["Animation", "Comedy", "Fantasy"],
        "rating": 7.9,
        "year": 2023,
        "description": "A group of magical animals go on a colorful adventure to save their enchanted forest."
    },
    {
        "title": "Cold Case Files",
        "genres": ["Crime", "Drama", "Mystery"],
        "rating": 8.1,
        "year": 2016,
        "description": "A retired detective reopens a decades-old unsolved case that changes everything."
    },
    {
        "title": "Space Odyssey Reborn",
        "genres": ["Sci-Fi", "Drama"],
        "rating": 8.6,
        "year": 2015,
        "description": "An astronaut stranded in deep space must find a way back home before time runs out."
    },
    {
        "title": "The Comedy Wedding",
        "genres": ["Comedy", "Romance"],
        "rating": 6.8,
        "year": 2021,
        "description": "Chaos erupts when two feuding families are forced to plan a wedding together."
    },
    {
        "title": "Iron Storm",
        "genres": ["Action", "Thriller"],
        "rating": 7.7,
        "year": 2020,
        "description": "A soldier races against time to stop a terrorist plot from destroying the city."
    },
    {
        "title": "Whispers of the Past",
        "genres": ["Drama", "Mystery"],
        "rating": 7.4,
        "year": 2019,
        "description": "A woman uncovers her family's hidden history after finding an old diary."
    },
    {
        "title": "The Documentary Project",
        "genres": ["Documentary"],
        "rating": 8.0,
        "year": 2022,
        "description": "An in-depth look into the lives of wildlife photographers around the world."
    },
    {
        "title": "Dragon's Legacy",
        "genres": ["Fantasy", "Action", "Adventure"],
        "rating": 8.9,
        "year": 2023,
        "description": "A hidden heir must tame an ancient dragon to reclaim the throne from a tyrant king."
    },
    {
        "title": "Night Terrors",
        "genres": ["Horror"],
        "rating": 6.5,
        "year": 2018,
        "description": "A group of friends trapped in an abandoned asylum must survive till dawn."
    },
]
