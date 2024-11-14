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

import os
import pathlib

import setuptools
import setuptools.command.build_py

here = pathlib.Path(__file__).parent.resolve()
about = {}
with open(os.path.join(here, "livekit", "plugins", "rime", "version.py"), "r") as f:
    exec(f.read(), about)


setuptools.setup(
    name="livekit-plugins-rime",
    version=about["__version__"],
    description="LiveKit Agents Plugin for Rime",
    long_description=(here / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/livekit/agents",
    cmdclass={},
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords=["webrtc", "realtime", "audio", "video", "livekit", "rime"],
    license="Apache-2.0",
    packages=setuptools.find_namespace_packages(include=["livekit.*"]),
    python_requires=">=3.9.0",
    install_requires=["livekit-agents[codecs]>=0.12.3"],
    package_data={"livekit.plugins.rime": ["py.typed"]},
    project_urls={
        "Documentation": "https://docs.livekit.io",
        "Website": "https://livekit.io/",
        "Source": "https://github.com/livekit/agents",
    },
)
# Modified on Tue Jan 21 11:33:41 PM +01 2025
print('Debug message')
# Modified on Tue Jan 21 11:33:54 PM +01 2025
print('Debug message')
