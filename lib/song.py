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

    # Property methods for validation
    @property
    def name(self):
        """Return the song's name."""
        return self._name

    @name.setter
    def name(self, value):
        """Validate and set the song's name."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Song name must be a non-empty string")
        self._name = value

    @property
    def artist(self):
        """Return the song's artist."""
        return self._artist

    @artist.setter
    def artist(self, value):
        """Validate and set the song's artist."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Artist name must be a non-empty string")
        self._artist = value

    @property
    def genre(self):
        """Return the song's genre."""
        return self._genre

    @genre.setter
    def genre(self, value):
        """Validate and set the song's genre."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Genre must be a non-empty string")
        self._genre = value

    # Class methods
    @classmethod
    def add_song_to_count(cls):
        """Increment the total song count."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls):
        """Add unique genres to the genres list."""
        # Convert genres list to a list of unique genres
        cls.genres = list(dict.fromkeys(cls.genres))

    @classmethod
    def add_to_artists(cls):
        """Add unique artists to the artists list."""
        # Convert artists list to a list of unique artists
        cls.artists = list(dict.fromkeys(cls.artists))

    @classmethod
    def add_to_genre_count(cls):
        """Update the genre_count dictionary with the number of songs per genre."""
        cls.genre_count = {}  # Reset dictionary
        for genre in cls.genres:
            cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls):
        """Update the artist_count dictionary with the number of songs per artist."""
        cls.artist_count = {}  # Reset dictionary
        for artist in cls.artists:
            cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
