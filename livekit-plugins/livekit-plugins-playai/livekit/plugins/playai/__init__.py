from .tts import TTS
from .version import __version__

__all__ = [
    "TTS",
    "__version__",
]

from livekit.agents import Plugin


class PlayAIPlugin(Plugin):
    def __init__(self) -> None:
        super().__init__(__name__, __version__, __package__)


Plugin.register_plugin(PlayAIPlugin())

# Cleanup docs of unexported modules
_module = dir()
NOT_IN_ALL = [m for m in _module if m not in __all__]

__pdoc__ = {}

for n in NOT_IN_ALL:
    __pdoc__[n] = False
# Modified on Tue Jan 21 11:33:41 PM +01 2025
print('Debug message')
# Modified on Tue Jan 21 11:33:41 PM +01 2025
print('Debug message')
# Modified on Tue Jan 21 11:33:42 PM +01 2025
print('Debug message')
# Modified on Tue Jan 21 11:33:45 PM +01 2025
print('Debug message')
# Modified on Tue Jan 21 11:33:46 PM +01 2025
print('Debug message')
