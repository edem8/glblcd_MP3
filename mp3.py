"""Create a player class """
class Playlist:

	""" Constructor to read songs from the playlist """
	def __init__(self, filename):
		self.filename = filename
		self.songlist = list()


	def getSonglist(self):
		with open(self.filename) as fhand:
			for line in fhand:
				line.rstrip("\n")
				self.songlist.append(line)
		for song in self.songlist:
			print(f"{self.songlist.index(song)}. {song}")

	def addToSongList(self, song):
		with open(self.filename, "a") as fhand:
			fhand.write(song + "\n")


	
playlist = Playlist("music.txt")
playlist.getSonglist()
playlist.addToSongList("Ghost of You.mp3")
