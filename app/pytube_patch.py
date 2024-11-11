from pytube import extract
from pytube import YouTube

def patched_get_signature(cipher: str, url: str):
    """
    Патч для исправления декодирования сигнатур.
    """
    js = YouTube(url).player_config_args["player_response"]["assets"]["js"]
    return extract.apply_signature(cipher, js)

YouTube.get_signature = patched_get_signature