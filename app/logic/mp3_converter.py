from pydub import AudioSegment
import base64
import io


def str_2_base64(s):
    base64_bytes = s.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes


def convert(data):
    keys = ["flac", "wav", "ogg"]
    b_track = None
    k = ""
    for key in keys:
        if key in data:
            k = key
            b_track = str_2_base64(data[key])

    audio_stream = io.BytesIO(b_track)
    audio_segment = AudioSegment.from_file(audio_stream, format=k)

    out_stream = io.BytesIO()
    track_handle = audio_segment.export(out_stream, format="mp3", bitrate="320k")

    return track_handle
