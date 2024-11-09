from typing import Literal

from pyht.client import Format  # type: ignore

TTSModel = Literal["Play3.0-mini", "PlayDialog"]
FORMAT = Literal["mp3"]
format_mapping = {
    "mp3": Format.FORMAT_MP3,
}
# Modified on Tue Jan 21 11:33:53 PM +01 2025
print('Debug message')
