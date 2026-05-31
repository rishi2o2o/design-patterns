from abc import ABC, abstractmethod
import random

# --- Collection Items ---
class Song:
    def __init__(self, title: str, artist: str, is_favorite: bool = False):
        self.title = title
        self.artist = artist
        self.is_favorite = is_favorite

    def __str__(self):
        return f"'{self.title}' by {self.artist}"

# --- Concrete Collection/Aggregate ---
class Playlist:
    """The central collection. It holds data but defers traversal to iterators."""
    def __init__(self, name: str):
        self.name = name
        self._songs: list[Song] = []

    def add_song(self, song: Song) -> None:
        self._songs.append(song)

    # --- Iterator Factories ---
    def get_sequential_iterator(self) -> 'SequentialSongIterator':
        return SequentialSongIterator(self._songs)

    def get_shuffled_iterator(self) -> 'ShuffledSongIterator':
        return ShuffledSongIterator(self._songs)

    def get_favorites_iterator(self) -> 'FavoriteSongIterator':
        return FavoriteSongIterator(self._songs)


# --- Iterator Interface ---
class SongIterator(ABC):
    @abstractmethod
    def hasNext(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> Song:
        pass

# --- Concrete Iterators ---

class SequentialSongIterator(SongIterator):
    """Iterates through songs from first to last."""
    def __init__(self, songs: list[Song]):
        self._songs = songs
        self._index = 0
    
    def hasNext(self) -> bool:
        if self._index < len(self._songs):
            return True
        return False
    
    def next(self) -> Song:
        song = self._songs[self._index]
        self._index += 1
        return song


class ShuffledSongIterator(SongIterator):
    """Iterates through songs in a random order."""
    def __init__(self, songs: list[Song]):
        self._shuffled_songs = songs.copy()
        random.shuffle(self._shuffled_songs)
        self._index = 0
    
    def hasNext(self) -> bool:
        if self._index < len(self._shuffled_songs):
            return True
        return False
    
    def next(self) -> Song:
        song = self._shuffled_songs[self._index]
        self._index += 1
        return song


class FavoriteSongIterator(SongIterator):
    """Iterates only through songs marked as favorites."""
    def __init__(self, songs: list[Song]):
        self._favorite_songs = [song for song in songs if song.is_favorite]
        self._index = 0
    
    def hasNext(self) -> bool:
        if self._index < len(self._favorite_songs):
            return True
        return False
    
    def next(self) -> Song:
        song = self._favorite_songs[self._index]
        self._index += 1
        return song
    

# --- Client Code ---

if __name__ == "__main__":

    # Create collection
    my_playlist = Playlist("Chill Vibes")

    # Add items to collection
    my_playlist.add_song(Song("Blinding Lights", "The Weeknd", is_favorite=True))
    my_playlist.add_song(Song("Bohemian Rhapsody", "Queen"))
    my_playlist.add_song(Song("Shape of You", "Ed Sheeran", is_favorite=True))
    my_playlist.add_song(Song("Hotel California", "Eagles"))

    # 1. Play all songs in order
    print("--- PLAYING ALL SONGS (SEQUENTIAL) ---")
    seq_iter = my_playlist.get_sequential_iterator()
    while seq_iter.hasNext():
        print(seq_iter.next())

    # 2. Play songs randomly
    print("\n--- PLAYING SHUFFLED TRACKS ---")
    shuf_iter = my_playlist.get_shuffled_iterator()
    while shuf_iter.hasNext():
        print(shuf_iter.next())

    # 3. Play only starred tracks
    print("\n--- PLAYING ONLY FAVORITES ---")
    fav_iter = my_playlist.get_favorites_iterator()
    while fav_iter.hasNext():
        print(fav_iter.next())



