"""Create a player class """
from random import shuffle

class Playlist:

	""" Constructor to read songs from the playlist """
	def __init__(self):
		self.songlist = []


	def getSonglist(self, filename):
		with open(filename) as fhand:
			self.songlist = [line.rstrip().split()[1] for line in fhand]
		for index, song in enumerate(self.songlist):
			print(f"{index}. {song}")

	def addToSongList(self, song):
		self.songlist.append(song)

	def removeSong(self, song):
		try:
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

	def calculateDuration(self):
		pass


 
playlist = Playlist()
playlist.addToSongList("Girls like you.mp3 2:22")
playlist.addToSongList("Hello.mp3 2:40")
playlist.addToSongList("Alone at the Top.mp3 2:12")
playlist.savePlaylist("music.txt")
playlist.getSonglist("music.txt")
playlist.removeSong("Alone at the Top.mp3")
print("/nAgain")
playlist.savePlaylist("music.txt")
playlist.getSonglist("music.txt")
print(playlist.songCount())

