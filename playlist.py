"""Create a player class """
from random import shuffle

class Playlist:

        """ Constructor to read songs from the playlist """
        def __init__(self):
                self.songlist = []


        def getSonglist(self, filename):
                with open(filename) as fhand:
                        self.songlist = [line.rstrip() for line in fhand]
                for index, song in enumerate(self.songlist):
                        splitString = song.split(',')
                        songName = splitString[0].strip()
                        print(f"{index}. {songName}")

        def addToSongList(self, song):
                self.songlist.append(song)

        def removeSong(self, songName):
                try:
                        for song in self.songlist:
                                if songName in song:
                                    self.songlist.remove(song)
                except ValueError:
                        print("Song not found")

        def shufflePlaylist(self):
                shuffle(self.songlist)

        def savePlaylist(self, filename):
                with open(filename, "w") as fhand:
                        for song in self.songlist:
                                fhand.write(song + "\n")
        def songCount(self):
                return len(self.songlist)

        def clearPlaylist(self):
                self.songlist.clear()

        def  isemptyPlaylist(self):
                return len(self.songlist) == 0
        
        def calculateDuration(self, filename):
                duration =[]
                minutes, seconds = 0, 0
                Tmins, Tsec = 0, 0
                with open(filename) as fhand:
                        duration= [line.strip().split(",")[1].strip() for line in fhand]
                for time in duration:
                    minutes, seconds = map(int, time.split(':'))
                    Tmins += minutes
                    Tsec += seconds
                Tmins += Tsec // 60
                Tsec %= 60
                print(f"Total duration is {Tmins}:{Tsec:02}")


playlist = Playlist()
playlist.addToSongList("Girls like you.mp3, 2:22")
playlist.addToSongList("Hello.mp3, 1:23")
playlist.addToSongList("Alone at the Top.mp3, 4:10")
playlist.savePlaylist("music.txt")
playlist.getSonglist("music.txt")

print("\n...shuffling...\n")
playlist.shufflePlaylist()
playlist.savePlaylist("music.txt")
playlist.getSonglist("music.txt")
playlist.savePlaylist("music.txt")

print("\n....removing a song...\n")
playlist.removeSong("Alone at the Top.mp3")
playlist.savePlaylist("music.txt")
playlist.getSonglist("music.txt")
playlist.savePlaylist("music.txt")

print("\n....printing duration of playlist...\n")
playlist.calculateDuration("music.txt")
