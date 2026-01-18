
def genres_for_query(top_mood):
    MOOD_TO_GENRES = {
    "sadness": [
        "Family",
        "Comedy",
        "Romance",
        "Drama",
        "Music",
        "Animation"
    ],

    "neutral": [
        "Drama",
        "Mystery",
        "Adventure",
        "Action",
        "Crime",
        "History",
        "Documentary",
        "Horror"
    ],

    "joy": [
        "Comedy",
        "Adventure",
        "Animation",
        "Fantasy",
        "Family",
        "Romance",
        "Action"
    ],

    "surprise": [
        "Adventure",
        "Mystery",
        "Thriller",
        "Science Fiction",
        "Fantasy",
        "Action",
        "Horror"
    ],

    "anger": [
        "Action",
        "Thriller",
        "Crime",
        "War",
        "Adventure"
    ],

    "fear": [
        "Family",
        "Comedy",
        "Animation",
        "Fantasy",
        "Music"
    ],

    "disgust": [
        "Comedy",
        "Family",
        "Animation",
        "Fantasy"
    ]
}

    mood=top_mood['label']
    mood_genres=MOOD_TO_GENRES.get(mood,["Comedy","Action"])
        
    return mood_genres



