from player import play_stream, play_file
from mic_streamer import stream
from synthesizer import synthesize_text


def handler(transcript):
    print(transcript)
    audio_content=synthesize_text(transcript)
    #print('audio content:', audio_content)
    play_stream(audio_content)


#stream(handler)
handler('가나다라')
