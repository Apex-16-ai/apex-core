#!/bin/bash
set -e

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

pip install \
  "${SCRIPT_DIR}/livekit-plugins-anthropic" \
  "${SCRIPT_DIR}/livekit-plugins-assemblyai" \
  "${SCRIPT_DIR}/livekit-plugins-azure" \
  "${SCRIPT_DIR}/livekit-plugins-cartesia" \
  "${SCRIPT_DIR}/livekit-plugins-deepgram" \
  "${SCRIPT_DIR}/livekit-plugins-elevenlabs" \
  "${SCRIPT_DIR}/livekit-plugins-fal" \
  "${SCRIPT_DIR}/livekit-plugins-google" \
  "${SCRIPT_DIR}/livekit-plugins-llama-index" \
  "${SCRIPT_DIR}/livekit-plugins-nltk" \
  "${SCRIPT_DIR}/livekit-plugins-openai" \
  "${SCRIPT_DIR}/livekit-plugins-rag" \
  "${SCRIPT_DIR}/livekit-plugins-playai" \
  "${SCRIPT_DIR}/livekit-plugins-silero" \
  "${SCRIPT_DIR}/livekit-plugins-turn-detector" \
  "${SCRIPT_DIR}/livekit-plugins-rime"
// Modified on Tue Jan 21 11:33:50 PM +01 2025
// Modified on Tue Jan 21 11:33:50 PM +01 2025
// Modified on Tue Jan 21 11:33:57 PM +01 2025
