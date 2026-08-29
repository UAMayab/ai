"""Raw interaction-log data for ReelWave (Session 7: Data -> Information -> Knowledge).

All rows are hand-authored (no randomness) so every student sees identical data
and the data-quality numbers are exactly reproducible for grading.
"""

import pandas as pd

BASE_LOGS = [
    # Kids profiles
    {"log_id": 1, "user_id": "u_k1", "profile_type": "kids", "date": "2026-09-01", "content_title": "Bunny Buddies", "genre": "Cartoon", "action": "watched", "rating": 5, "genre_match_score": 0.82},
    {"log_id": 2, "user_id": "u_k1", "profile_type": "kids", "date": "2026-09-01", "content_title": "Sparkle Ponies", "genre": "Cartoon", "action": "watched", "rating": 4, "genre_match_score": 0.78},
    {"log_id": 3, "user_id": "u_k2", "profile_type": "kids", "date": "2026-09-02", "content_title": "Puppy Playhouse", "genre": "Cartoon", "action": "watched", "rating": 5, "genre_match_score": 0.80},
    {"log_id": 4, "user_id": "u_k2", "profile_type": "kids", "date": "2026-09-02", "content_title": "Space Explorers", "genre": "SciFi", "action": "watched", "rating": 4, "genre_match_score": 0.70},
    {"log_id": 5, "user_id": "u_k3", "profile_type": "kids", "date": "2026-09-03", "content_title": "Bunny Buddies", "genre": "Cartoon", "action": "rated", "rating": 5, "genre_match_score": 0.85},
    {"log_id": 6, "user_id": "u_k3", "profile_type": "kids", "date": "2026-09-03", "content_title": "Midnight Slasher", "genre": "Horror", "action": "watched", "rating": 1, "genre_match_score": 0.91},
    {"log_id": 7, "user_id": "u_k4", "profile_type": "kids", "date": "2026-09-04", "content_title": "Sparkle Ponies", "genre": "Cartoon", "action": "watched", "rating": 5, "genre_match_score": 0.79},
    {"log_id": 8, "user_id": "u_k4", "profile_type": "kids", "date": "2026-09-04", "content_title": "Puppy Playhouse", "genre": "Cartoon", "action": "watched", "rating": 4, "genre_match_score": 0.76},
    # Teen profiles
    {"log_id": 9, "user_id": "u_t1", "profile_type": "teen", "date": "2026-09-01", "content_title": "Teen Drama High", "genre": "Drama", "action": "watched", "rating": 4, "genre_match_score": 0.74},
    {"log_id": 10, "user_id": "u_t1", "profile_type": "teen", "date": "2026-09-01", "content_title": "Space Explorers", "genre": "SciFi", "action": "watched", "rating": 5, "genre_match_score": 0.77},
    {"log_id": 11, "user_id": "u_t2", "profile_type": "teen", "date": "2026-09-02", "content_title": "Teen Drama High", "genre": "Drama", "action": "rated", "rating": 3, "genre_match_score": 0.68},
    {"log_id": 12, "user_id": "u_t2", "profile_type": "teen", "date": "2026-09-02", "content_title": "Comedy Nights", "genre": "Comedy", "action": "watched", "rating": 4, "genre_match_score": 0.72},
    {"log_id": 13, "user_id": "u_t3", "profile_type": "teen", "date": "2026-09-03", "content_title": "Space Explorers", "genre": "SciFi", "action": "watched", "rating": 4, "genre_match_score": 0.75},
    {"log_id": 14, "user_id": "u_t3", "profile_type": "teen", "date": "2026-09-03", "content_title": "Teen Drama High", "genre": "Drama", "action": "watched", "rating": 5, "genre_match_score": 0.80},
    {"log_id": 15, "user_id": "u_t4", "profile_type": "teen", "date": "2026-09-04", "content_title": "Comedy Nights", "genre": "Comedy", "action": "watched", "rating": 3, "genre_match_score": 0.66},
    {"log_id": 16, "user_id": "u_t4", "profile_type": "teen", "date": "2026-09-04", "content_title": "Teen Drama High", "genre": "Drama", "action": "watched", "rating": 4, "genre_match_score": 0.73},
    # Adult profiles
    {"log_id": 17, "user_id": "u_a1", "profile_type": "adult", "date": "2026-09-01", "content_title": "Midnight Slasher", "genre": "Horror", "action": "watched", "rating": 5, "genre_match_score": 0.88},
    {"log_id": 18, "user_id": "u_a1", "profile_type": "adult", "date": "2026-09-01", "content_title": "Haunted Manor", "genre": "Horror", "action": "watched", "rating": 4, "genre_match_score": 0.84},
    {"log_id": 19, "user_id": "u_a2", "profile_type": "adult", "date": "2026-09-02", "content_title": "Cooking with Chef Lupe", "genre": "Cooking", "action": "watched", "rating": 5, "genre_match_score": 0.81},
    {"log_id": 20, "user_id": "u_a2", "profile_type": "adult", "date": "2026-09-02", "content_title": "Comedy Nights", "genre": "Comedy", "action": "watched", "rating": 4, "genre_match_score": 0.71},
    {"log_id": 21, "user_id": "u_a3", "profile_type": "adult", "date": "2026-09-03", "content_title": "Haunted Manor", "genre": "Horror", "action": "watched", "rating": 5, "genre_match_score": 0.86},
    {"log_id": 22, "user_id": "u_a3", "profile_type": "adult", "date": "2026-09-03", "content_title": "Cooking with Chef Lupe", "genre": "Cooking", "action": "rated", "rating": 4, "genre_match_score": 0.79},
    {"log_id": 23, "user_id": "u_a4", "profile_type": "adult", "date": "2026-09-04", "content_title": "Comedy Nights", "genre": "Comedy", "action": "watched", "rating": 3, "genre_match_score": 0.69},
    {"log_id": 24, "user_id": "u_a4", "profile_type": "adult", "date": "2026-09-04", "content_title": "Midnight Slasher", "genre": "Horror", "action": "watched", "rating": 5, "genre_match_score": 0.89},
    # Corrupted: missing ratings
    {"log_id": 25, "user_id": "u_k1", "profile_type": "kids", "date": "2026-09-05", "content_title": "Space Explorers", "genre": "SciFi", "action": "watched", "rating": None, "genre_match_score": 0.72},
    {"log_id": 26, "user_id": "u_t2", "profile_type": "teen", "date": "2026-09-05", "content_title": "Space Explorers", "genre": "SciFi", "action": "watched", "rating": None, "genre_match_score": 0.74},
    {"log_id": 27, "user_id": "u_a1", "profile_type": "adult", "date": "2026-09-05", "content_title": "Comedy Nights", "genre": "Comedy", "action": "watched", "rating": None, "genre_match_score": 0.68},
    {"log_id": 28, "user_id": "u_k3", "profile_type": "kids", "date": "2026-09-05", "content_title": "Puppy Playhouse", "genre": "Cartoon", "action": "watched", "rating": None, "genre_match_score": 0.77},
    # Additional clean rows
    {"log_id": 29, "user_id": "u_t1", "profile_type": "teen", "date": "2026-09-06", "content_title": "Comedy Nights", "genre": "Comedy", "action": "watched", "rating": 4, "genre_match_score": 0.70},
    {"log_id": 30, "user_id": "u_a2", "profile_type": "adult", "date": "2026-09-06", "content_title": "Haunted Manor", "genre": "Horror", "action": "watched", "rating": 5, "genre_match_score": 0.87},
]

# Corrupted: exact duplicate log entries (same event logged twice)
DUPLICATE_LOG_IDS = [1, 5, 9, 17, 21, 24]
DUPLICATES = [dict(row) for row in BASE_LOGS if row["log_id"] in DUPLICATE_LOG_IDS]

ALL_LOGS = BASE_LOGS + DUPLICATES


def get_raw_logs() -> pd.DataFrame:
    return pd.DataFrame(ALL_LOGS)


def get_data_quality_report(df: pd.DataFrame) -> dict:
    duplicate_rows = int(df.duplicated().sum())
    missing_ratings = int(df["rating"].isna().sum())
    return {
        "total_rows": len(df),
        "duplicate_rows": duplicate_rows,
        "missing_ratings": missing_ratings,
        "total_corrupted": duplicate_rows + missing_ratings,
    }
