class Song:
    # Class attributes
    count = 0  # Tracking total number of songs
    genres = []  # List to store all genres (duplicates allowed initially)
    artists = []  # List to store all artists (duplicates allowed initially)
    genre_count = {}  # Dictionary to store genre histogram
    artist_count = {}  # Dictionary to store artist histogram

    def __init__(self, name, artist, genre):
        """
        Initialize a Song instance with name, artist, and genre.
        Updates class-level tracking of songs, artists, genres, and counts.
        """
        # Instance attributes
        self._name = name
        self._artist = artist
        self._genre = genre

        # Add to class-level tracking
        Song.genres.append(genre)  # Adds genre to genres list
        Song.artists.append(artist)  # Adds artist to artists list

        # Calls class methods to update counts and lists (unique)
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    