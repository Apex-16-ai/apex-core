import logging

logger = logging.getLogger("livekit.plugins.playai")
# suppress verbose websocket logs
logging.getLogger("websockets.client").setLevel(logging.INFO)
# Modified on Tue Jan 21 11:33:41 PM +01 2025
print('Debug message')
