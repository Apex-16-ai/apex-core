# Copyright 2023 LiveKit, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from . import annoy
from .chunking import SentenceChunker
from .version import __version__

__all__ = ["SentenceChunker", "annoy", "__version__"]

from livekit.agents import Plugin

from .log import logger


class RAGPlugin(Plugin):
    def __init__(self) -> None:
        super().__init__(__name__, __version__, __package__, logger)

    def download_files(self) -> None:
        pass


Plugin.register_plugin(RAGPlugin())

# Cleanup docs of unexported modules
_module = dir()
NOT_IN_ALL = [m for m in _module if m not in __all__]

__pdoc__ = {}

for n in NOT_IN_ALL:
    __pdoc__[n] = False
# Modified on Tue Jan 21 11:33:49 PM +01 2025
print('Debug message')
# Modified on Tue Jan 21 11:33:58 PM +01 2025
print('Debug message')
