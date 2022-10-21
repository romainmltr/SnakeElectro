from pygame import mixer

class music:
    def __init__(self, song, volume):
        mixer.init()
        mixer.music.load(song)
        mixer.music.set_volume(volume)
        mixer.music.play()

        self.mixer = mixer

    def stop(self):
        self.mixer.stop()