import random

# Create a node class for each song holding the data of the song name
class Song:
    # There are 3 attributes, a pointer to the previous node, a pointer
    # to the next node, and the data of the node
    def __init__(self, song_name=None, next_song=None, prev_song=None):
        self.song_name = song_name
        self.prev_song = prev_song
        self.next_song = next_song
        
class Playlist:
    def __init__(self):
        self.first_song = None
    
    # This function adds a new song to the end of the playlist
    def addSong(self, song_name):

        song_to_add = Song(song_name)
        current_song = self.first_song
        song_to_add.next_song = None
        
        # If the playlist is empty make the new song the first song
        if (self.first_song is None):
            self.first_song = song_to_add
            song_to_add.prev_song = None
        # If it is not empty then go to the very end and add add it
        else:
            # go to the end of the list
            while(current_song.next_song is not None):
                current_song = current_song.next_song
            
            #add the song
            current_song.next_song = song_to_add
            song_to_add.prev_song = current_song
            
    # This function prints the name of the songs separated by a newline char
    def printSongs(self):
        temp = self.first_song
        song_string = ""
        while (temp is not None):
            song_string = song_string + temp.song_name
            song_string = song_string + '\n'
            temp = temp.next_song
        return song_string
    
    # This function returns the length of the playlist
    def getLength(self):
        length = 0
        current_song = self.first_song
        
        # Count until it reaches the end of the list
        while (current_song is not None):
            length = length + 1
            current_song = current_song.next_song
        return length
        
    # This function will select and return a random song in the playlist
    def randomSong(self):
        song_to_play = self.first_song
        # Chooses a random number between = and the length of the playlist
        rand_num = random.randint(0, self.getLength())
        for num in range(0,rand_num):
            if (song_to_play.next_song is not None):
                song_to_play = song_to_play.next_song
        return song_to_play
    
    # This method finds the last node and returns it
    def lastSong(self):
        temp_song = self.first_song
        while(temp_song.next_song is not None):
            temp_song = temp_song.next_song
        return temp_song
    
    # This function reverses the playlist by changing each pointer and then
    # changing the pointer to the first song
    def reversePlaylist(self):
        
        current_song = self.first_song
        temparary_song = None
        
        while (current_song is not None):
            # Swap the pointers for each song using a temp variable
            temparary_song = current_song.prev_song
            current_song.prev_song = current_song.next_song
            current_song.next_song = temparary_song
            current_song = current_song.prev_song
        
        # set the last song equal to the first song
        if (temparary_song is not None):
            self.first_song = temparary_song.prev_song
