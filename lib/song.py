class Song:
    # Class attributes
    count = 0  # Tracking total number of songs
    genres = []  # List to store all genres (with duplicates)
    artists = []  # List to store all artists (with duplicates)
    unique_genres = set()  # Store unique genres
    unique_artists = set()  # Store unique artists
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
        Song.count += 1
        Song.genres.append(genre)  # Keep duplicates for counting
        Song.artists.append(artist)  # Keep duplicates for counting
        Song.unique_genres.add(genre)  # Track unique genres
        Song.unique_artists.add(artist)  # Track unique artists
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1

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

  
