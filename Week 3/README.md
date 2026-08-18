# Project 3: Movie Recommendation System

A simple, content-based recommendation system built in **pure Python** (no
external libraries needed). It takes a user's preferences (genres or
free-text keywords) and recommends the most relevant movies from a sample
dataset using similarity-based logic.

---

## 1. Project Overview

| | |
|---|---|
| **Project Name** | Movie Recommendation System |
| **Type** | Console-based (CLI) Application |
| **Language** | Python 3 |
| **Core Concepts** | Logic building, Pattern Matching, Recommendation Systems |
| **Dependencies** | None (Python standard library only) |

The system demonstrates **content-based filtering** — a recommendation
approach that suggests items based on how similar their attributes (genres,
description, etc.) are to what the user is interested in, rather than
relying on other users' behavior (which is how *collaborative filtering*
works).

---

## 2. Features

- Take user preferences as input (genre selection or free-text keywords)
- Two independent matching/recommendation strategies:
  1. **Genre-based matching** using **Cosine Similarity**
  2. **Keyword-based matching** using **Pattern Matching**
- Ranks and displays the **top N recommended movies** with a match score
- View the entire movie catalog
- Simple, menu-driven, beginner-friendly command-line interface
- Clean, modular code split across multiple files for readability

---

## 3. Project Structure

```
project3_recommendation_system/
│
├── data.py          # Sample movie dataset (title, genres, rating, description)
├── recommender.py   # Core recommendation logic (RecommendationEngine class)
├── main.py          # CLI entry point — handles user input & output display
└── README.md        # Project documentation (this file)
```

---

## 4. How It Works (Algorithm Explanation)

### 4.1 Genre-Based Recommendation — Cosine Similarity

1. All unique genres in the dataset are collected (e.g., Action, Comedy,
   Drama, Sci-Fi, ...).
2. The user selects their favourite genres from a numbered list.
3. Both the **user's interests** and **each movie's genres** are converted
   into binary vectors over the full genre space.

   Example (genre space = `[Action, Comedy, Drama]`):
   - User picks `Comedy` → vector = `[0, 1, 0]`
   - Movie has genres `[Comedy, Drama]` → vector = `[0, 1, 1]`

4. **Cosine Similarity** is calculated between the two vectors:

   ```
   similarity = (A · B) / (||A|| × ||B||)
   ```

   This returns a value between `0` (no match) and `1` (perfect match).

5. A **final score** is calculated to slightly reward higher-rated movies:

   ```
   final_score = (similarity × 0.85) + (normalized_rating × 0.15)
   ```

6. Movies are sorted by final score, and the **top 5** are shown.

### 4.2 Keyword-Based Recommendation — Pattern Matching

1. The user types free-text interests (e.g., `dragon, king, war`).
2. Each keyword is searched for inside every movie's **description +
   genres** (case-insensitive substring/pattern matching).
3. A **match ratio** is calculated:

   ```
   match_ratio = (keywords found) / (total keywords entered)
   ```

4. Final score combines match ratio with rating:

   ```
   final_score = (match_ratio × 0.90) + (normalized_rating × 0.10)
   ```

5. Movies are sorted by final score, and the **top 5** are shown.

---

## 5. How to Run

**Requirements:** Python 3.7 or higher (no external packages needed)

```bash
cd project3_recommendation_system
python main.py
```

You will see a menu:

```
=======================================================
              MOVIE RECOMMENDATION SYSTEM
=======================================================
1. Recommend by selecting genres
2. Recommend by typing keywords/interests
3. View all movies
4. Exit
```

- Choose **1** to pick genres from a numbered list (e.g. `1,4,7`)
- Choose **2** to type free-text keywords (e.g. `space, future, robot`)
- Choose **3** to view the full movie catalog
- Choose **4** to exit

---

## 6. Example Run

**Input:** Genres → `Action, Crime, Horror`

**Output:**

```
Top 5 Recommendation(s):

#  Title                     Genres                      Rating  Match Score
------------------------------------------------------------------------------------------
1  Night Terrors             Horror                      6.5     0.588
2  Iron Storm                Action, Thriller            7.7     0.463
3  Haunted Hollow            Horror, Thriller            6.9     0.451
4  Dragon's Legacy           Fantasy, Action, Adventure  8.9     0.417
5  The Last Kingdom Rises    Fantasy, Adventure, Action  8.8     0.415
```

**Input:** Keywords → `dragon, king, war`

**Output:**

```
Top 2 Recommendation(s):

#  Title                     Genres                      Rating  Match Score
------------------------------------------------------------------------------------------
1  Dragon's Legacy           Fantasy, Action, Adventure  8.9     0.689
2  The Last Kingdom Rises    Fantasy, Adventure, Action  8.8     0.688
```

---

## 7. Key Skills Demonstrated

- **Logic Building** — designing scoring formulas, ranking, and menu flow
- **Pattern Matching** — keyword/substring search across text fields
- **Recommendation Concepts** — content-based filtering, similarity
  scoring (cosine similarity), vector representation of categorical data

---

## 8. Possible Future Improvements

- Load the dataset from a CSV/JSON file or a real API instead of hardcoding it
- Add a GUI (e.g., using Tkinter or a web interface with Flask)
- Include collaborative filtering using ratings from multiple users
- Use TF-IDF weighting instead of simple binary genre vectors
- Add user profiles that save preferences across sessions

---

## 9. Author Notes

This project was built as **Project 3**, focusing on demonstrating core
recommendation-system logic (similarity/pattern matching) in a clean,
well-documented, and dependency-free way so it can run on any machine with
Python installed.
