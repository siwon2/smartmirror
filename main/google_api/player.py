
import vlc
from pydub import AudioSegment
from pydub.playback import play
import io

def play_file(audio_file):
	instance = vlc.Instance()
	player = instance.media_player_new()

	media = instance.media_new(audio_file)

	player.set_media(media)

	player.play()
	
	
	while player.get_state() != vlc.State.Ended:
		pass
#time.sleep(10)
def play_stream(audio_stream):
    song = AudioSegment.from_file(io.BytesIO(audio_stream), format="mp3",frame_rate=24000)

    play(song)
    return 
	
