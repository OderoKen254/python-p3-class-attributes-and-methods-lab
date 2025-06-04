class Song:
    # Class attributes
    count = 0  # Tracking total number of songs
    genres = []  # List to store all genres (duplicates allowed initially)
    artists = []  # List to store all artists (duplicates allowed initially)
    genre_count = {}  # Dictionary to store genre histogram
    artist_count = {}  # Dictionary to store artist histogram

    