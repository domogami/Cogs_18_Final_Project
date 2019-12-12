import pytest
from functions import *

# Tests the Song class
def TestMySong():
    My_Song = Song("myJam")
    assert isinstance(My_Song.song_name, str)
    assert My_Song.song_name == "myJam"

TestMySong()

# Tests the playlist class and all of its methods

def TestMyPlaylist():
    # Test Playlist class
    AwesomeMixtape = Playlist()
    assert isinstance(AwesomeMixtape, Playlist)
    
    # Test addSong()
    AwesomeMixtape.addSong("Song1")
    AwesomeMixtape.addSong("Song2")
    AwesomeMixtape.addSong("Song3")
    AwesomeMixtape.addSong("Song4")
    assert AwesomeMixtape.first_song.song_name == "Song1"


    # Test printSongs()
    assert "Song1\nSong2\nSong3\nSong4\n" == AwesomeMixtape.printSongs()

    # Test getLength()
    assert (4 == AwesomeMixtape.getLength())

    # Test randomSong()
    song = AwesomeMixtape.randomSong()
    assert isinstance(song,Song)

    # Test lastSong()
    assert "Song4" == AwesomeMixtape.lastSong().song_name

    # Test reversePlaylist()
    AwesomeMixtape.reversePlaylist()
    assert "Song4\nSong3\nSong2\nSong1\n" == AwesomeMixtape.printSongs()

TestMyPlaylist()
